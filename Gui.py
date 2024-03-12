from PyQt5 import QtCore, QtWidgets
# ТУТ ВСЁ - ДИЗАЙН

class Ui_Gui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 587)
        MainWindow.setMinimumSize(QtCore.QSize(797, 587))
        MainWindow.setMaximumSize(QtCore.QSize(797, 587))
        MainWindow.setStyleSheet(
            """QComboBox {
     border: 1px solid gray;
     border-radius: 3px;
     padding: 1px 18px 1px 3px;
     min-width: 6em;
 }

 QComboBox:editable {
     background: white;
 }

 QComboBox:!editable, QComboBox::drop-down:editable {
      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                  stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                  stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
 }

 /* QComboBox получает состояние "on", когда всплывающий список раскрыт */
 QComboBox:!editable:on, QComboBox::drop-down:editable:on {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                 stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
 }

 QComboBox:on { /* сдвиг текста, когда раскрывается всплывающий список */
     padding-top: 3px;
     padding-left: 4px;
 }

 QComboBox::drop-down {
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 15px;

     border-left-width: 1px;
     border-left-color: darkgray;
     border-top-right-radius: 3px; /* тот же радиус закругления что и у QComboBox */
     border-bottom-right-radius: 3px;
 }


 QComboBox::down-arrow:on { /* сдвиг стрелки, когда раскрывается всплывающий список */
     top: 1px;
     left: 1px;
 }"""
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 801, 611))
        self.label.setText("")
        self.label.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 60, 570, 200))
        self.textEdit.setStyleSheet(
            'font:14pt "Myanmar Text";\n' "background-color: rgb(255, 255, 255)"
        )
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(325, 509, 140, 51))
        self.pushButton.setStyleSheet(
            "border-radius: 20px;\n"
            "background-color: rgb(255, 68, 6);\n"
            'font: 75 10pt "Myanmar Text";'
        )
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 291, 22))
        self.label_2.setStyleSheet("color: rgb(255, 68, 6);")
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(400, 270, 280, 22))
        self.comboBox_2.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n color: rgb(255, 68, 6);\n"
        )
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 270, 291, 22))
        self.label_3.setStyleSheet("\n" "color: rgb(255, 68, 6);")
        self.label_3.setObjectName("label_3")
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(400, 30, 280, 22))
        self.comboBox_1.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n color: rgb(255, 68, 6);\n"
        )
        self.comboBox_1.setCurrentText("")
        self.comboBox_1.setObjectName("comboBox_1")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 300, 570, 200))
        self.textEdit_2.setStyleSheet(
            'font:14pt "Myanmar Text";\n' "background-color: rgb(255, 255, 255)"
        )
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 250, 61, 61))
        self.pushButton_2.setStyleSheet(
            "border-radius: 30px;\n"
            'font: 75 8pt "Myanmar Text";\n'
            "background-color: rgb(255, 68, 6);"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton_3.setStyleSheet(
            "border-radius: 14px;\n" "background-color: rgb(255, 68, 6);"
        )
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(730, 20, 30, 30))
        self.pushButton_4.setStyleSheet(
            'font: 9pt "NSimSun";\n'
            "background-color: rgb(255, 68, 6);\n"
            "border-radius: 15px"
        )
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Write your text."))
        self.pushButton.setText(_translate("MainWindow", "Перевести"))
        self.label_2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">Выбери язык:</p></body></html>',
            )
        )
        self.label_3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">Выбери язык:</p></body></html>',
            )
        )
        self.textEdit_2.setPlaceholderText(
            _translate("MainWindow", "Look at the translation.")
        )
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_3.setText(_translate("MainWindow", "←Вернуться"))
        self.pushButton_4.setText(_translate("MainWindow", "i"))


# ################################################################################################################################
# ################################################################################################################################
# ################################################################################################################################
class Ui_GGui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setText("")
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.OutText = QtWidgets.QTextEdit(self.centralwidget)
        self.OutText.setEnabled(False)
        self.OutText.setGeometry(QtCore.QRect(200, 270, 400, 50))
        self.OutText.setStyleSheet(
            'font: 14pt "Trebuchet MS";\n' "\n" "border: 3px solid"
        )
        self.OutText.setObjectName("OutText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 325, 100, 40))
        self.label_2.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.459776, cy:0.517, radius:2, fx:0.5, fy:0.5, stop:0 rgba(252, 252, 252, 107), stop:1 rgba(255, 255, 255, 0));\n"
            "border-radius:20px"
        )
        self.label_2.setObjectName("label_2")
        self.InputText = QtWidgets.QTextEdit(self.centralwidget)
        self.InputText.setGeometry(QtCore.QRect(260, 370, 280, 40))
        self.InputText.setStyleSheet(
            'font: 75 10pt "Yu Gothic UI";\n' "border: 3px solid"
        )
        self.InputText.setObjectName("InputText")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(175, 220, 450, 40))
        self.label_3.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.459776, cy:0.517, radius:2, fx:0.5, fy:0.5, stop:0 rgba(252, 252, 252, 107), stop:1 rgba(255, 255, 255, 0));\n"
            "border-radius:15px"
        )
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 420, 100, 40))
        self.pushButton.setStyleSheet(
            "background-color: rgb(255, 68, 6);\n"
            'font: 75 10pt "Segoe UI";\n'
            "border-radius:14px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border: 2px solid"
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 5, 100, 40))
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 68, 6);\n"
            'font: 75 10pt "Segoe UI";\n'
            "border-radius:14px;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border: 2px solid"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(765, 5, 30, 30))
        self.pushButton_4.setStyleSheet(
            'font: 9pt "NSimSun";\n'
            "background-color: rgb(255, 68, 6);\n"
            "border-radius: 15px"
        )
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 470, 281, 40))
        self.label_4.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.459776, cy:0.517, radius:2, fx:0.5, fy:0.5, stop:0 rgba(252, 252, 252, 107), stop:1 rgba(255, 255, 255, 0));\n"
            "border-radius:15px"
        )
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 120, 221, 40))
        self.label_5.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.459776, cy:0.517, radius:2, fx:0.5, fy:0.5, stop:0 rgba(252, 252, 252, 107), stop:1 rgba(255, 255, 255, 0));\n"
            "border-radius:15px"
        )
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OutText.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Trebuchet MS'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:12px; font-size:8pt;"><br /></p></body></html>',
            )
        )
        self.OutText.setPlaceholderText(
            _translate("MainWindow", "Тут появится слово на английском.")
        )
        self.label_2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600;">Перевод:</span></p></body></html>',
            )
        )
        self.InputText.setPlaceholderText(
            _translate("MainWindow", "Введите перевод слова.")
        )
        self.label_3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">Слово на английском для перевода:</span></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("MainWindow", "Проверить"))
        self.pushButton_2.setText(_translate("MainWindow", "←Выйти   "))
        self.pushButton_4.setText(_translate("MainWindow", "i"))
        self.label_4.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">Решено 0 из 0</span></p></body></html>',
            )
        )
        self.label_5.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600;">Время: 00:00</span></p></body></html>',
            )
        )


# #########################################################################################################################################
# #########################################################################################################################################
# #########################################################################################################################################
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(60, 160, 100, 30))
        self.comboBox.setStyleSheet("background-color: rgb(255, 68, 6);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 160, 100, 30))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 68, 6);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        Form.setStyleSheet(
            """
                           QComboBox {
     border-radius: 3px;
     padding: 1px 18px 1px 3px;
     min-width: 6em;
 }

 QComboBox:editable {
     background: white;
 }

 QComboBox:!editable, QComboBox::drop-down:editable {
      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                  stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                  stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
 }

 /* QComboBox получает состояние "on", когда всплывающий список раскрыт */
 QComboBox:!editable:on, QComboBox::drop-down:editable:on {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                 stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
 }


 QComboBox::drop-down {
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 15px;

     border-left-width: 1px;
     border-left-color: darkgray;
     border-top-right-radius: 3px; /* тот же радиус закругления что и у QComboBox */
     border-bottom-right-radius: 3px;
 }


 QComboBox::down-arrow:on { /* сдвиг стрелки, когда раскрывается всплывающий список */
     top: 1px;
     left: 1px;
 }"""
        )
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 70, 211, 71))
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 121, 31))
        self.pushButton.setStyleSheet(
            "border-radius: 15px;\n"
            "background-color:rgb(255, 68, 6);\n"
            "border: 2px solid"
        )
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "A1"))
        self.comboBox.setItemText(1, _translate("Form", "B1"))
        self.comboBox.setItemText(2, _translate("Form", "C1"))
        self.comboBox_2.setItemText(0, _translate("Form", "5"))
        self.comboBox_2.setItemText(1, _translate("Form", "10"))
        self.comboBox_2.setItemText(2, _translate("Form", "25"))
        self.comboBox_2.setItemText(3, _translate("Form", "50"))
        self.comboBox_2.setItemText(4, _translate("Form", "75"))
        self.label.setText(
            _translate(
                "Form",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600;">Выбери уровень и</span></p><p align="center"><span style=" font-size:12pt; font-weight:600;">количество слов</span></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("Form", "OK"))


# #########################################################################################################################################
# #########################################################################################################################################
# #########################################################################################################################################
class Ui_Save(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(242, 130)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: black")
        self.OKsave = QtWidgets.QPushButton(self.centralwidget)
        self.OKsave.setGeometry(QtCore.QRect(80, 90, 81, 31))
        self.OKsave.setObjectName("OKsave")
        self.OKsave.setStyleSheet(
            "background-color: rgb(255, 68, 6);\n" "border-radius: 15px"
        )
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 221, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" 'font: 75 12pt "Segoe UI";\n'
        )
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 101, 20))
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: rgb(255, 68, 6)")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OKsave.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "Введите имя:"))
