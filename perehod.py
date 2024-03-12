from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QRegion
from PyQt5.QtWidgets import QMainWindow
from Gui import Ui_Form
from translator_game import MainGame


class Perehodnik(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        # переходник в игру переводчик
        super(Perehodnik, self).__init__(parent)
        self.setupUi(self)
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
        self.pushButton.clicked.connect(self.okay)

    def okay(self):
        # передача выбранных данных игре для выбора нужного словаря и количества слов
        lvl = self.comboBox.currentText()
        e = self.comboBox_2.currentText()
        self.ex = MainGame(self, lvl=lvl, e=e)
        self.ex.show()
        self.hide()
