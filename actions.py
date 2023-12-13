import sqlite3
import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QLabel, QWidget, QLineEdit, QTextEdit

from request_selection import Requests
from del_account import Delete


class Actions(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Действия с аккаунтом')

        self.what_action = QLabel(self)
        self.what_action.move(10, 10)
        self.what_action.resize(110, 20)
        self.what_action.setText('Выберите действие:')

        self.facts_btn = QPushButton('Получить факты', self)
        self.facts_btn.resize(130, 30)
        self.facts_btn.move(10, 40)
        self.facts_btn.clicked.connect(self.facts)

        self.history_btn = QPushButton('Просмотреть историю', self)
        self.history_btn.resize(130, 30)
        self.history_btn.move(10, 80)
        self.history_btn.clicked.connect(self.history)

        self.del_history_btn = QPushButton('Очистить историю', self)
        self.del_history_btn.resize(130, 30)
        self.del_history_btn.move(10, 120)
        self.del_history_btn.clicked.connect(self.delete_history)

        self.del_account_btn = QPushButton('Удалить аккаунт', self)
        self.del_account_btn.resize(130, 30)
        self.del_account_btn.move(10, 160)
        self.del_account_btn.clicked.connect(self.delete_account)

        self.cancel_btn = QPushButton('Закрыть', self)
        self.cancel_btn.resize(55, 30)
        self.cancel_btn.move(435, 160)
        self.cancel_btn.clicked.connect(self.cancellation)

        self.history_lbl = QLabel(self)
        self.history_lbl.move(150, 10)
        self.history_lbl.resize(70, 20)
        self.history_lbl.setText('История:')

        self.user_history = QTextEdit(self)
        self.user_history.setEnabled(False)
        self.user_history.resize(340, 110)
        self.user_history.move(150, 40)

    def facts(self):
        self.request = Requests(self)
        self.request.show()
        self.close()

    def history(self):
        amt = 0
        con = sqlite3.connect("users.sql")
        cur = con.cursor()
        self.username = ''
        name = cur.execute("""SELECT user FROM information WHERE choice = ''""")
        for i in name:
            self.username += str(i[0])

        self.history_info = []
        self.history_data = cur.execute("""SELECT * FROM information WHERE user = ? AND choice NOT LIKE ''""",
                                        (self.username,))
        for i in self.history_data:
            self.history_info.append(i[2:])

        if len(self.history_info) == 0:
            self.user_history.setText('История пустая.')

        else:
            self.result_history = ''
            for i in self.history_info:
                amt += 1
                self.result_history += f'{amt}. Выбраный тип факта: {i[0]}.\n'
                self.result_history += f'   Значение: {i[1]}\n'
                self.result_history += f'   Полученный факт: {i[2]}.\n'
                if i[3] != None:
                    self.result_history += f'   Заметка: {i[3]}\n'
                self.result_history += f'------------------------------------------------------------------------------\n'

            self.user_history.setText(self.result_history)
            self.user_history.setEnabled(True)

        con.close()

    def delete_history(self):
        self.user_history.clear()

        con = sqlite3.connect("users.sql")
        cur = con.cursor()
        self.username = ''
        name = cur.execute("""SELECT user FROM information WHERE choice = ''""")
        for i in name:
            self.username += str(i[0])
        cur.execute("""DELETE FROM information WHERE user = ? AND choice NOT LIKE ''""",
                    (self.username,))

        con.commit()
        con.close()

    def delete_account(self):
        self.del_acc = Delete(self)
        self.del_acc.show()

    def cancellation(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Actions()
    ex.show()
    sys.exit(app.exec())