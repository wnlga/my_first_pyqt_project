import googletrans
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from Gui import Ui_Gui
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QRegion
from lk import LANGUAGESS


class Main(QMainWindow, Ui_Gui):
    def __init__(self, parent=None):
        # дизайн
        super(Main, self).__init__(parent)
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
        self.textEdit.clear()
        self.add_languages()
        self.pushButton.clicked.connect(self.translate)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.info)
        self.pushButton_3.clicked.connect(self.returnToStart)

    def info(self):
        # информация о переводчике
        msg = QMessageBox()
        text = """                          Информация к использованию:
        Для того, чтобы перевести текст используйте поле для ввода, находящееся сверху, укажите язык, который вводите, для ибежания ошибки, и выберите текст на который хотите перевести.
    После выполнения действий описанных выше нажмите кнопку "Перевести" для выполнения перевода введенного текста.
    Для очищения полей ввода и вывода нажмите "Очистить".
    Чтобы вернуться к предыдущему окну нажмите "Вернуться".
    Приятного использования!:)"""
        msg.setWindowTitle("Информация")
        msg.setText(str(text))
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def add_languages(self):
        # возможнось выбора нескольких языков
        for x in LANGUAGESS.values():
            self.comboBox_1.addItem(x)
            self.comboBox_2.addItem(x)

    def translate(self):
        # перевод введенного текста
        try:
            translator = googletrans.Translator()
            input_text = self.textEdit.toPlainText()
            for key, value in LANGUAGESS.items():
                if value == self.comboBox_1.currentText():
                    language_1 = key
                    break
            for key, value in LANGUAGESS.items():
                if value == self.comboBox_2.currentText():
                    language_2 = key
                    break
            translate = translator.translate(
                input_text, src=language_1, dest=language_2
            )
            self.textEdit_2.setText(translate.text)
        except Exception as e:
            self.error_message(e)

    def error_message(self, text):
        # вывод ошибки при неудаче
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText(str(text))
        msg.exec_()

    def clear(self):
        # очищение полей ввода и вывода
        self.textEdit.clear()
        self.textEdit_2.clear()

    def returnToStart(self):
        # возвращение на родину
        self.parent().show()
        self.close()
