from Gui import Ui_Save
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QRegion
import sqlite3


class SaveResultDialog(QMainWindow, Ui_Save):
    def __init__(self, parent=None, lvl="A1", n_words=5, time=None):
        # дизайн
        super(SaveResultDialog, self).__init__(parent)
        self.lvl = lvl
        self.setupUi(self)
        self.ttable = "words_" + str(n_words)
        self.n_words = n_words
        self.time = time[:2] + "." + time[3:]
        self.setWindowFlag(Qt.FramelessWindowHint)
        radius = 10
        base = self.rect()
        ellipse = QRect(0, 0, 2 * radius, 2 * radius)
        base_region = QRegion(base.adjusted(radius, 0, -radius, 0))
        base_region |= QRegion(base.adjusted(0, radius, 0, -radius))
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveTopRight(base.topRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomRight(base.bottomRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomLeft(base.bottomLeft())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        self.setMask(base_region)
        self.OKsave.clicked.connect(self.getName)
        self.checkText()

    def checkText(self):
        # проверка введенного никнейма на корректность текста для избежания ошибок
        alf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        text = self.textEdit.toPlainText()
        self.atext = ""
        for i in text:
            if i in alf:
                self.atext += i

    def getName(self):
        # сохранение результата в базе данных
        bd = self.lvl + "_scores.db"
        self.checkText()
        con = sqlite3.connect(bd)
        input_t = self.atext if len(self.atext) <= 10 else self.atext[:11]
        cur = con.cursor()
        cur.execute(
            f"""INSERT INTO {self.ttable} (name, time) VALUES ('{input_t}', '{self.time}')"""
        )
        con.commit()
        con.close()
        self.parent().parent().parent().show()
        self.hide()
