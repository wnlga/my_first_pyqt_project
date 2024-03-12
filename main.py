from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QRegion
from translator import Main
from perehod import Perehodnik
from MouseGame import MyWidget
from recordTable import RecordTable
from Notepad import NoteApp
import sqlite3
from Gui import Ui_Form


class MyStartWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # создание кнопок и дизайна в общем
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.setObjectName("MainWindow")
        self.setFixedSize(719, 349)
        self.setStyleSheet("background-color: rgb(0, 0, 0);\n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.startMouseGame = QtWidgets.QPushButton(self.centralwidget)
        self.startMouseGame.setGeometry(QtCore.QRect(177, 280, 380, 50))
        self.startMouseGame.setFont(font)
        self.check_bd()
        self.startMouseGame.setStyleSheet(
            "border-radius: 15px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 68, 6);"
        )
        self.startMouseGame.setObjectName("startMouseGame")
        self.showRecord = QtWidgets.QPushButton(self.centralwidget)
        self.showRecord.setGeometry(QtCore.QRect(524, 5, 190, 40))
        self.showRecord.setStyleSheet(
            'font:10pt "Century Gothic";\n'
            "border-radius: 14px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 68, 6);"
        )
        self.showRecord.setObjectName("startMouseGame")
        self.startWork = QtWidgets.QPushButton(self.centralwidget)
        self.startWork.setGeometry(QtCore.QRect(60, 225, 300, 50))
        self.startWork.setFont(font)
        self.startWork.setStyleSheet(
            "border-radius: 15px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 68, 6);"
        )
        self.startWork.setObjectName("startWork")
        self.startGame = QtWidgets.QPushButton(self.centralwidget)
        self.startGame.setGeometry(QtCore.QRect(365, 225, 300, 50))
        self.startGame.setFont(font)
        self.startGame.setStyleSheet(
            "border-radius: 15px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(255, 68, 6);"
        )
        self.startGame.setObjectName("startWork")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 60, 711, 151))
        self.label.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            'font: 75 italic 16pt "Candara";\n'
            "border-radius: 15"
        )
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 5, 100, 40))
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 68, 6);\n"
            'font: 75 10pt "Segoe UI";\n'
            "border-radius:14px;\n"
            "border-color: rgb(0, 0, 0);\n"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("←Выйти   ")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(5, 50, 100, 40))
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(255, 68, 6);\n"
            'font: 75 10pt "Segoe UI";\n'
            "border-radius:14px;\n"
            "border-color: rgb(0, 0, 0);\n"
        )
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Заметки")
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
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
        self.startWork.clicked.connect(self.startwork)
        self.startGame.clicked.connect(self.startgame)
        self.startMouseGame.clicked.connect(self.startmousegame)
        self.pushButton_2.clicked.connect(lambda: exit())
        self.pushButton_3.clicked.connect(self.opennote)
        self.showRecord.clicked.connect(self.showrecord)

    def startwork(self):
        # запуск переводчика
        self.hide()
        self.window = Main(self)
        self.window.show()
    
    def opennote(self):
        # открытие заметок
        self.hide()
        self.window = NoteApp(self)
        self.window.show()

    def showrecord(self):
        # открытие переходника в таблицу
        self.hide()
        self.window = PerehodTable(self)
        self.window.show()

    def startgame(self):
        # открытие переходника в игру-переводчика
        self.hide()
        self.window = Perehodnik(self)
        self.window.show()

    def startmousegame(self):
        # открытие игры "убегающая кнопка"
        self.hide()
        self.window = MyWidget(self)
        self.window.show()
    
    def check_bd(self):
        # проверка целостности таблицы
        bds = ['A1_scores.db', 'B1_scores.db', 'C1_scores.db']
        ww = ['words_5', 'words_10', 'words_25', 'words_50', 'words_75']
        for i in bds:
            con = sqlite3.connect(i)
            cur = con.cursor()
            for table in ww:
                cur.execute(f'''CREATE TABLE IF NOT EXISTS {table} (
                            name text,
                            time text
                )''')
                con.commit()
            con.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startWork.setText(_translate("MainWindow", "Зайти в переводчик"))
        self.startMouseGame.setText(_translate("MainWindow", "Потренировать скорость"))
        self.showRecord.setText(_translate("MainWindow", "Посмотреть рекорды"))
        self.startGame.setText(_translate("MainWindow", "Зайти в игру"))
        self.label.setText(
            _translate(
                "MainWindow",
                """<html><head/><body><p align=\"center\"><span style=\" font-family:\'Verdana\';
                                       font-size:14pt; font-weight:400; font-style:normal;\">Добро пожаловать!</span></p><p align=\"center\"><span style=\" font-family:\'Verdana\';
                                       font-size:14pt; font-weight:400; font-style:normal;\"> Выберите, чем хотите заняться.</span></p><p align=\"center\">
                                      <span style=\" font-family:\'Verdana\'; font-size:14pt; font-weight:400; font-style:normal;\">Нажмите на кнопку, чтобы начать.</span></p></body></html>""",
            )
        )


class PerehodTable(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        # переходник в таблицу рекордов
        # создание дизайна
        super(PerehodTable, self).__init__(parent)
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
        # передача данных таблице и её открытие
        lvl = self.comboBox.currentText()
        e = self.comboBox_2.currentText()
        self.ex = RecordTable(self, lvl=lvl, e=e)
        self.ex.show()
        self.hide()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    ex = MyStartWidget()
    ex.show()
    sys.exit(app.exec_())
