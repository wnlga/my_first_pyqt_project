import sqlite3
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableView, QPushButton


class RecordTable(QMainWindow):
    def __init__(self, parent=None, lvl="A1", e="5"):
        # дизайн
        super(RecordTable, self).__init__(parent)
        self.lvl = lvl + "_scores.db"
        self.e = "words_" + e
        self.setStyleSheet("background-color: rgb(255, 255, 255)")
        if not QSqlDatabase.database().isOpen():
            self.db = QSqlDatabase.addDatabase("QSQLITE")
        else:
            self.db = QSqlDatabase.database()
        self.db.setDatabaseName(self.lvl)
        self.db.open()
        # отбражение данных
        view = QTableView(self)
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable(self.e)
        self.model.sort(1, Qt.AscendingOrder)
        self.model.select()
        view.setEnabled(False)
        view.setModel(self.model)
        view.move(0, 0)
        view.resize(300, 600)
        self.clearButton = QPushButton(self)
        self.clearButton.setGeometry(0, 600, 270, 40)
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setText("Удалить все данные")
        self.clearButton.clicked.connect(self.clearRecord)

        self.setFixedSize(270, 640)
        self.setWindowTitle("Таблица рекордов")

    def clearRecord(self):
        # удалить рекорды из выбранной таблицы
        con = sqlite3.connect(self.lvl)
        cur = con.cursor()
        cur.execute(f"drop table {self.e}")
        cur.execute(
            f"""create table {self.e} (
            name text,
            time text
            )"""
        )
        con.commit()
        con.close()
        self.model.setTable(self.e)
        self.model.select()
        self.update()

    def closeEvent(self, event):
        # при закрытии таблицы возвращение на стартовое окно
        self.db.close()
        self.parent().parent().show()
