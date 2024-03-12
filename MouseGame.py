import random
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal, QRect, Qt
from PyQt5.QtGui import QRegion


class Button(QPushButton):
    mouseMoved = pyqtSignal()

    def mouseMoveEvent(self, event):
        self.mouseMoved.emit()


class MyWidget(QMainWindow):
    def __init__(self, parent=None):
        # дизайн
        super(MyWidget, self).__init__(parent)
        self.click_n = 0
        self.setWindowFlag(Qt.FramelessWindowHint)
        radius = 10
        self.w = 500
        self.h = 400
        self.setGeometry(675, 400, self.w, self.h)
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
        self.centralwidget = QMainWindow(self)
        self.centralwidget.setObjectName("centralwidget")
        self.coords = [40, 40]
        self.btn_size = [120, 40]
        self.d = 15

        self.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            """QPushButton#evilButton:pressed {
    background-color: rgb(224, 0, 0);
    border-style: inset;
}"""
        )
        self.setWindowTitle("Убегающая кнопка")
        self.button = Button(self)
        self.button.setMouseTracking(True)
        self.button.setText("Нажми меня")
        self.button.resize(*self.btn_size)
        self.button.move(*self.coords)
        self.button.mouseMoved.connect(self.moveButton)
        self.button.setStyleSheet(
            """
QPushButton#evilButton:pressed {
    background-color: rgb(224, 0, 0);
    border-style: inset;
}"""
        )
        self.button.setStyleSheet(
            "border-radius: 14px;\n"
            "background-color: rgb(255, 68, 6);\n"
            'font: 75 10pt "Myanmar Text";'
        )
        self.button.clicked.connect(self.end)

    def end(self):
        # конец игры
        msg = QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText(
            f"""Ваш резултат:
У вас не получилось {self.click_n} раз
                    """
        )
        msg.setIcon(QMessageBox.Information)

        self.hide()
        self.parent().show()
        msg.exec_()

    def moveButton(self):
        # изменение координат кнопки при столкновении с курсором
        self.coords[0] = random.randint(0, self.w - self.btn_size[0])
        self.coords[1] = random.randint(0, self.h - self.btn_size[1])
        self.button.move(*self.coords)

    def mousePressEvent(self, event):
        # считывание количества неудачных нажатий ЛКМ
        if event.button() == Qt.LeftButton:
            self.click_n += 1
