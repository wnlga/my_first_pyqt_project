from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextEdit, QFileDialog
from PyQt5 import QtCore

class NoteApp(QMainWindow):
    def __init__(self, parent=None):
        # дизайн
        super(NoteApp, self).__init__(parent)
        self.setWindowTitle('Заметки')
        self.setGeometry(100, 100, 600, 445)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n")

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(5, 5, 590, 365)
        self.btn_save = QPushButton('Сохранить', self)
        self.btn_save.setGeometry(QtCore.QRect(250, 410, 100, 30))

        self.btn_save.clicked.connect(self.save_notes)

        self.btn_choose_file = QPushButton('Выбрать файл', self)
        self.btn_choose_file.clicked.connect(self.choose_file)
        self.btn_choose_file.setGeometry(QtCore.QRect(225, 375, 150, 30))



        self.btn_save.setStyleSheet(
            'font: 75 10pt "Segoe UI";\n'
            "border: 1px solid;\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 10px;\n"
        )
        self.btn_choose_file.setStyleSheet(
            "border: 1px solid;\n"
            'font: 75 10pt "Segoe UI";\n'
            "border-color: rgb(0, 0, 0);\n"
            "border-radius: 10px;\n"
        )


        self.current_file = None  # Для хранения текущего выбранного файла

    def save_notes(self):
        # сохранение файла с текстовой заметкой
        text = self.text_edit.toPlainText()
        if not text:
            return  # Не сохраняем, если текст пуст

        if self.current_file is None:
            self.choose_file_for_save()
            return

        with open(self.current_file + '.txt' if '.txt' not in self.current_file else self.current_file, 'w') as file:
            file.write(text)

    def choose_file(self):
        # выбор файла с текстовыми заметками
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', 'Text Files (*.txt);;All Files (*)', options=options)
        self.text_edit.clear()
        if file_name:
            with open(file_name, 'r') as file:
                self.text_edit.setPlainText(file.read())
            self.current_file = file_name

    def choose_file_for_save(self):
        # выбор файла/названия файла для сохранения сохранения заметки
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить заметки', '', 'Text Files (*.txt);;All Files (*)', options=options)

        if file_name:
            self.current_file = file_name
            self.save_notes()
    
    def closeEvent(self, event):
        # возвращение на родину при закрытии
        self.parent().show()
