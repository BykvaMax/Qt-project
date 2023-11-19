import sys
import sqlite3

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit

from actions import Actions


class Entry(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.args = args
        self.setGeometry(300, 300, 255, 135)
        if self.args[-1] == 'Вход':
            self.setWindowTitle('Вход')
        else:
            self.setWindowTitle('Регистрация')

        self.username = QLabel(self)
        self.username.move(10, 10)
        self.username.resize(105, 20)
        self.username.setText('Введите своё имя:')

        self.input_username = QLineEdit(self)
        self.input_username.setEnabled(True)
        self.input_username.move(115, 10)

        self.password = QLabel(self)
        self.password.move(10, 35)
        self.password.resize(105, 20)
        self.password.setText('Введите пароль:')

        self.input_password = QLineEdit(self)
        self.input_password.setEnabled(True)
        self.input_password.move(115, 35)

        self.error = QLabel(self)
        self.error.move(10, 65)
        self.error.resize(250, 20)

        self.back_btn = QPushButton('Назад', self)
        self.back_btn.resize(50, 30)
        self.back_btn.move(10, 95)
        self.back_btn.clicked.connect(self.backward)

        self.ok_btn = QPushButton('ОК', self)
        self.ok_btn.resize(30, 30)
        self.ok_btn.move(150, 95)
        self.ok_btn.clicked.connect(self.confirmation)

        self.cancel_btn = QPushButton('Закрыть', self)
        self.cancel_btn.resize(55, 30)
        self.cancel_btn.move(190, 95)
        self.cancel_btn.clicked.connect(self.cancellation)

    def confirmation(self):
        if self.args[-1] == 'Вход':
            con = sqlite3.connect("users.sql")
            cur = con.cursor()
            names = cur.execute("""SELECT name FROM users_data""").fetchall()
            usernames = []
            for i in names:
                usernames.append(str(i[0]))

            if self.input_username.text() not in usernames or len(self.input_username.text()) == 0:
                self.error.setText('Пользователя нет в БД, либо ошибка ввода.')

            else:
                self.error.clear()
                password = cur.execute("""SELECT password FROM users_data WHERE name = ?""",
                                   (self.input_username.text(),)).fetchall()

            if (self.input_username.text() in usernames and self.input_password.text() != str(password[0][0])):
                self.error.setText('Ошибка в имени пользователя или в пароле.')

            elif self.input_username.text() in usernames and self.input_password.text() == str(password[0][0]):
                names = cur.execute("""SELECT user FROM information WHERE choice = ''""").fetchall()
                usernames = []
                for i in names:
                    usernames.append(str(i[0]))
                if self.input_username.text() not in usernames:
                    name = """INSERT INTO information(user, choice, data, result) VALUES (?, ?, ?, ?);"""
                    cur.execute(name, (self.input_username.text(), '', '', ''))

                self.action = Actions(self)
                self.action.show()
                self.close()

            con.commit()
            con.close()

        elif self.args[-1] == 'Регистрация':
            if self.input_username.text() == 'Guest':
                self.error.setText('Такое имя пользователя не допускается.')

            else:
                con = sqlite3.connect("users.sql")
                cur = con.cursor()
                data = cur.execute("""SELECT name FROM users_data """).fetchall()
                usernames = []
                for i in data:
                    usernames.append(str(i[0]))

                if self.input_username.text() in usernames:
                    self.error.setText('Имя уже занято.')

                else:
                    if len(self.input_username.text()) == 0 or len(self.input_password.text()) == 0:
                        self.error.setText('Ошибка в имени пользователя или в пароле.')

                    else:
                        original = """INSERT INTO users_data(name, password) VALUES (?, ?);"""
                        cur.execute(original, (self.input_username.text(), self.input_password.text()))

                        names = cur.execute("""SELECT user FROM information WHERE choice = ''""").fetchall()
                        usernames = []
                        for i in names:
                            usernames.append(str(i[0]))
                        if self.input_username.text() not in usernames:
                            name = """INSERT INTO information(user, choice, data, result) VALUES (?, ?, ?, ?);"""
                            cur.execute(name, (self.input_username.text(), '', '', ''))

                        self.action = Actions(self)
                        self.action.show()
                        self.close()

                con.commit()
                con.close()

    def backward(self):
        from login_method import Login
        self.back = Login(self)
        self.back.show()
        self.close()

    def cancellation(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Entry()
    ex.show()
    sys.exit(app.exec())