import sqlite3
import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QLabel, QWidget

from request_selection import Requests
from entry_form import Entry


class Login(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 170, 160)
        self.setWindowTitle('Тип входа')

        self.type_of_login = QLabel(self)
        self.type_of_login.move(10, 10)
        self.type_of_login.resize(130, 20)
        self.type_of_login.setText('Выберите способ входа:')

        self.login_btn = QPushButton('Вход', self)
        self.login_btn.resize(90, 30)
        self.login_btn.move(10, 40)
        self.login_btn.clicked.connect(self.login)

        self.registration_btn = QPushButton('Регистрация', self)
        self.registration_btn.resize(90, 30)
        self.registration_btn.move(10, 80)
        self.registration_btn.clicked.connect(self.login)

        self.registration_btn = QPushButton('Как гость', self)
        self.registration_btn.resize(90, 30)
        self.registration_btn.move(10, 120)
        self.registration_btn.clicked.connect(self.guest)

        self.cancel_btn = QPushButton('Закрыть', self)
        self.cancel_btn.resize(55, 30)
        self.cancel_btn.move(110, 120)
        self.cancel_btn.clicked.connect(self.cancellation)

        con = sqlite3.connect("users.sql")
        cur = con.cursor()

        cur.execute("""DELETE FROM information WHERE choice = ''""")

        con.commit()
        con.close()

    def login(self):
        self.entry = Entry(self, self.sender().text())
        self.entry.show()
        self.close()

    def guest(self):
        con = sqlite3.connect("users.sql")
        cur = con.cursor()
        self.username = ''
        name = """INSERT INTO information(user, choice, data, result) VALUES (?, ?, ?, ?);"""
        cur.execute(name, ('Guest', '', '', ''))

        con.commit()
        con.close()
        self.request = Requests(self)
        self.request.show()
        self.close()

    def cancellation(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec())
