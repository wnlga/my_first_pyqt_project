from Gui import Ui_GGui
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QRegion
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from lk import ENGLISH_WORDS_A1, ENGLISH_WORDS_B1, ENGLISH_WORDS_C1
import random
from SaveResult import SaveResultDialog


class MainGame(QMainWindow, Ui_GGui):
    def __init__(self, parent=None, lvl="", e=""):
        # создание дизайна игры-переводчика
        self._translate = QtCore.QCoreApplication.translate
        self.stoptime = False
        super(MainGame, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.OutText = QtWidgets.QTextEdit(self.centralwidget)
        self.OutText.setEnabled(False)
        self.OutText.setGeometry(QtCore.QRect(200, 270, 400, 50))
        self.OutText.setStyleSheet(
            'font: 14pt "Trebuchet MS";\n'
            "background-color: rgb(255, 255, 255);"
            "\n"
            "border: 3px solid"
        )
        self.InputText = QtWidgets.QTextEdit(self.centralwidget)
        self.InputText.setGeometry(QtCore.QRect(260, 370, 280, 40))
        self.InputText.setStyleSheet(
            'font: 75 10pt "Yu Gothic UI";\n'
            "background-color: rgb(255, 255, 255);"
            "border: 3px solid"
        )
        self.InputText.setObjectName("textEdit_2")
        radius = 10
        base = self.rect()
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)
        if self.stoptime is False:
            self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)
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
        self.n = 0
        self.OutText.clear()
        self.InputText.clear()
        self.m = 0
        self.pushButton_2.clicked.connect(self.returnToStart)
        self.pushButton_4.clicked.connect(self.info)
        self.pushButton.clicked.connect(self.checkTranslation)
        self.lvl = lvl
        self.e = e
        self.getItems(self.lvl, self.e)
        self.min = 0
        self.sec = 0

    def timerEvent(self):
        # отображение и запись времени игры
        self.time = self.time.addSecs(1)
        self.ttime = self.time.toString("mm:ss")
        self.label_5.setText(
            self._translate(
                "MainWindow",
                f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Время: {self.time.toString('mm:ss')}</span></p></body></html>",
            )
        )

    def info(self):
        # отображение информации об игре
        msg = QMessageBox()
        text = """                          Информация игры:
    Суть игры заключается в том, чтобы пользователь мог развлечься и проверить свой уровень знания английского языка.
    Для того, чтобы начать играть нужно на начальном окне нажать соответствующую кнопку, после чего откроется окно для выбора уровня владения английским языком и количества слов.
    Приятной игры!:)"""
        msg.setWindowTitle("Информация")
        msg.setText(str(text))
        msg.setIcon(QMessageBox.Information)

        msg.exec_()

    def getItems(self, lvl, e):
        # выбор нужного словаря относительно выбранного уровня и нужного количества слов
        if lvl == "A1":
            self.words = list(random.sample(list(ENGLISH_WORDS_A1.keys()), int(e)))
            self.dicte = ENGLISH_WORDS_A1
        elif lvl == "B1":
            self.words = list(random.sample(list(ENGLISH_WORDS_B1.keys()), int(e)))
            self.dicte = ENGLISH_WORDS_B1
        else:
            self.words = list(random.sample(list(ENGLISH_WORDS_C1.keys()), int(e)))
            self.dicte = ENGLISH_WORDS_C1
        self.showWord()

    def checkTranslation(self):
        # проверка введенного перевода
        input_text = self.InputText.toPlainText().lower()
        i = self.OutText.toPlainText()
        englishWord = self.dicte[i]
        if input_text == englishWord:
            self.n += 1
        self.m += 1
        self.InputText.clear()
        self.label_4.setText(
            self._translate(
                "MainWindow",
                f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">Решено {self.n} из {self.m}</span></p></body></html>',
            )
        )
        if self.words != []:
            self.showWord()
        else:
            self.stoptime = True
            self.tttime = self.ttime
            self.endGame()

    def returnToStart(self):
        # возвращение на начальное окно
        self.parent().parent().show()
        self.close()

    def showWord(self):
        # отображение слова, которое нужно перевести
        self.OutText.setText(str(self.words.pop(0)))

    def endGame(self):
        # окончание игры и предоставление выбора о сохранении результата пользователя
        msg = QMessageBox()
        self.hide()
        text = f"""Игра окончена!
Ваш результат {self.n} из {self.m} слов, за {self.ttime}.
Желаете сохранить результат?"""
        msg.setWindowTitle("Игра окончена!")
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setIcon(QMessageBox.Question)
        msg.button(QMessageBox.Yes).setText("Да")
        msg.button(QMessageBox.No).setText("Нет")

        if msg.exec_() == QMessageBox.No:
            self.parent().parent().show()
            self.close()
        else:
            if self.n == self.m:
                self.ex = SaveResultDialog(
                    self, lvl=self.lvl, n_words=self.m, time=self.tttime
                )
                self.ex.show()
            else:
                ms = QMessageBox()
                txt = "Попробуйте ещё!"
                ms.setText(txt)
                ms.setWindowTitle("Игра окончена!")
                ms.setIcon(QMessageBox.Information)
                ms.exec_()
                self.parent().parent().show()

            self.hide()
