import sys
import sqlite3

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QApplication, QLabel, QWidget, QTextEdit
from translate import Translator
from PyQt5.QtCore import Qt

from data_get import Receiving
from note import Note



class Facts(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.received_info = Receiving.get_info(self, args)
        if self.received_info == 'error':
            self.setGeometry(300, 300, 500, 200)
            self.setWindowTitle('Ошибка')

            self.error_txt = QLabel(self)
            self.error_txt.move(10, 10)
            self.error_txt.resize(250, 20)
            self.error_txt.setText('Произошла ошибка при обработке запроса.')

            self.reasons = QLabel(self)
            self.reasons.move(10, 40)
            self.reasons.resize(130, 20)
            self.reasons.setText('Возможные причины:')

            self.site_unavailability = QLabel(self)
            self.site_unavailability.move(10, 70)
            self.site_unavailability.resize(350, 20)
            self.site_unavailability.setText('1. Недоступность сайта(тех. работы, сайт закрыт, и т. д.).')

            self.incorrect_values = QLabel(self)
            self.incorrect_values.move(10, 100)
            self.incorrect_values.resize(200, 20)
            self.incorrect_values.setText('2. Вы ввели значения неверно.')

            self.trouble_solving = QLabel(self)
            self.trouble_solving.move(10, 130)
            self.trouble_solving.resize(450, 20)
            self.trouble_solving.setText('Возможные варианты решения проблемы:')

            self.trouble_solving = QLabel(self)
            self.trouble_solving.move(10, 150)
            self.trouble_solving.resize(450, 20)
            self.trouble_solving.setText('1. Попробуйте ввести другие значения.')

            self.trouble_solving = QLabel(self)
            self.trouble_solving.move(10, 170)
            self.trouble_solving.resize(450, 20)
            self.trouble_solving.setText('2. Попробуйте зайти через некоторое время.')

            self.image = 'error.png'
            self.error_img = QPixmap(self.image)
            self.error_img = self.error_img.scaled(180, 180, Qt.KeepAspectRatio)

            self.error = QLabel(self)
            self.error.move(320, 10)
            self.error.setPixmap(self.error_img)

        else:
            con = sqlite3.connect("users.sql")
            cur = con.cursor()
            self.username = ''
            name = cur.execute("""SELECT user FROM information WHERE choice = ''""")
            for i in name:
                self.username += str(i[0])

            cur.execute("""DELETE FROM information WHERE choice = ''""")
            con.commit()
            con.close()

            self.check_save = False
            self.check_note = False
            self.info = args
            self.setGeometry(300, 300, 440, 270)
            self.setWindowTitle('Факт')

            self.fact = self.received_info[0]

            self.fact_type = QLabel(self)
            self.fact_type.move(10, 10)
            self.fact_type.resize(400, 20)
            self.fact_type.setText(f'Тип факта: {args[1]}')

            self.fact_txt = QLabel(self)
            self.fact_txt.move(10, 70)
            self.fact_txt.resize(50, 20)
            self.fact_txt.setText('Факт:')

            self.fact_line = QTextEdit(self)
            self.fact_line.setEnabled(False)
            self.fact_line.resize(250, 100)
            self.fact_line.move(10, 100)

            self.del_acc_error1 = QLabel(self)
            self.del_acc_error1.move(10, 210)
            self.del_acc_error1.resize(3000, 20)

            self.del_acc_error2 = QLabel(self)
            self.del_acc_error2.move(10, 225)
            self.del_acc_error2.resize(3000, 20)

            self.del_acc_error3 = QLabel(self)
            self.del_acc_error3.move(10, 240)
            self.del_acc_error3.resize(3000, 20)

            if self.username == '':
                self.username = 'Удалённый аккаунт'
                self.del_acc_error1.setText('Так как вы удалили свой аккаунт,')
                self.del_acc_error2.setText('для дальнейшей работы в приложении вам необходимо')
                self.del_acc_error3.setText('зарегестрироваться снова!')

            if self.username == 'Guest':
                self.del_acc_error1.setText('Так как вы зашли как гость,')
                self.del_acc_error2.setText('вам недоступны действия с аккаунтом, а также')
                self.del_acc_error3.setText('функции сохранения в БД и добавления заметки.')


            if (args[1] == 'Получить мудреный факт о числе' or args[1] == 'Получить примитивный факт о числе'
                    or args[1] == 'Получить факт о годе'):
                self.number = QLabel(self)
                self.number.move(10, 40)
                self.number.resize(2500, 20)
                self.number.setText(f'Введённое число: {args[2]}')

                self.fact_line.setText(Translator(to_lang='ru').translate(self.fact['text'].title()))

            elif args[1] == 'Получить факт о дате':
                self.date = f'{args[3]}.{args[2]}'
                self.month = QLabel(self)
                self.month.move(10, 40)
                self.month.resize(120, 20)
                self.month.setText(f'Введённый месяц: {args[2]}')

                self.day = QLabel(self)
                self.day.move(140, 40)
                self.day.resize(120, 20)
                self.day.setText(f'Введённый день: {args[3]}')

                if int(self.fact['year']) > 0:
                    self.fact_line.setText(f"В {self.fact['year']} году:\n"
                                           f"{Translator(to_lang='ru').translate(self.fact['text'].title())}")

                else:
                    self.fact_line.setText(f"В {str(self.fact['year'])[1:]} году до нашей эры:\n"
                                           f"{Translator(to_lang='ru').translate(self.fact['text'].title())}")

            elif args[1] == 'Получить рандомный факт':
                self.random_number = QLabel(self)
                self.random_number.move(10, 40)
                self.random_number.resize(2500, 20)

                if self.received_info[1] == 'year':
                    self.random_number.setText(f'Рандомное число: {self.fact["number"]}')
                    if int(self.fact['number']) > 0:
                        if len(self.fact) == 5:
                            self.fact_line.setText(f"В {self.fact['number']} году,"
                                                   f"{Translator(to_lang='ru').translate(self.fact['data'])}:\n"
                                                   f"{Translator(to_lang='ru').translate(self.fact['text'].title())}")
                        else:
                            self.fact_line.setText(f"В {self.fact['number']} году:\n"
                                                   f"{Translator(to_lang='ru').translate(self.fact['text'].title())}")

                    else:
                        if len(self.fact) == 5:
                            self.fact_line.setText(f"В {str(self.fact['number'])[1:]} году до нашей эры,"
                                                   f"{Translator(to_lang='ru').translate(self.fact['data'])}:\n"
                                                   f"{Translator(to_lang='ru').translate(self.fact['text'].title())}")
                        else:
                            self.fact_line.setText(f"В {str(self.fact['number'])[1:]} году до нашей эры:\n"
                                                   f"{Translator(to_lang='ru').translate(self.fact['text'].title())}")

                elif self.received_info[1] == 'date':
                    self.random_number.setText(f'Рандомное число: {self.fact["year"]}')
                    if int(self.fact['year']) > 0:
                        self.fact_line.setText(f"В {self.fact['year']} году:\n"
                                               f"{Translator(to_lang='ru').translate(self.fact['text'].title())}")

                    else:
                        self.fact_line.setText(f"В {str(self.fact['year'])[1:]} году до нашей эры:\n"
                                               f"{Translator(to_lang='ru').translate(self.fact['text'].title())}")

                elif self.received_info[1] == 'math' or self.received_info[1] == 'trivia':
                    self.random_number.setText(f'Рандомное число: {self.fact["number"]}')

                    self.fact_line.setText(Translator(to_lang='ru').translate(self.fact['text'].title()))

            self.save_btn = QPushButton('Сохранить в базу данных', self)
            self.save_btn.resize(160, 30)
            self.save_btn.move(270, 10)
            self.save_btn.clicked.connect(self.save)

            self.note_btn = QPushButton('Добавить заметку', self)
            self.note_btn.resize(160, 30)
            self.note_btn.move(270, 50)
            self.note_btn.clicked.connect(self.add_note)

            self.to_account_btn = QPushButton('Перейти к аккаунту', self)
            self.to_account_btn.resize(160, 30)
            self.to_account_btn.move(270, 130)
            self.to_account_btn.clicked.connect(self.action_form)

            self.to_requests_btn = QPushButton('Перейти к выбору факта', self)
            self.to_requests_btn.resize(160, 30)
            self.to_requests_btn.move(270, 90)
            self.to_requests_btn.clicked.connect(self.requests_form)

            if self.username == 'Guest' or self.username == 'Удалённый аккаунт':
                self.save_btn.setEnabled(False)
                self.note_btn.setEnabled(False)
                self.to_account_btn.setEnabled(False)
                if self.username == 'Удалённый аккаунт':
                    self.to_requests_btn.setEnabled(False)

            self.to_login_btn = QPushButton('Перейти ко входу в аккаунт', self)
            self.to_login_btn.resize(160, 30)
            self.to_login_btn.move(270, 170)
            self.to_login_btn.clicked.connect(self.login_form)

            self.cancel_btn = QPushButton('Закрыть', self)
            self.cancel_btn.resize(75, 40)
            self.cancel_btn.move(355, 220)
            self.cancel_btn.clicked.connect(self.cancellation)

    def write_logs(self):
        with open('logs.txt', 'a') as logs:
            result = ''
            if (self.info[1] == 'Получить мудреный факт о числе'
                    or self.info[1] == 'Получить примитивный факт о числе'
                    or self.info[1] == 'Получить факт о годе'):
                result += f'Пользователь: {self.username}\n'
                result += f'Выбраный тип факта: {self.info[1]}.\n'
                result += f'Значение: {self.info[2]}\n'
                result += f'Полученный факт: {Translator(to_lang="ru").translate(self.fact["text"].title())}.\n'
                result += f'Добавил заметку: {"Да" if self.check_note else "Нет"}\n'
                result += f'Сохранил в базу данных: {"Да" if self.check_save else "Нет"}\n'
                result += f'-----------------------------------------------------------------------------------------\n'
                logs.write(result)

            elif self.info[1] == 'Получить факт о дате':
                result += f'Пользователь: {self.username}\n'
                result += f'Выбраный тип факта: {self.info[1]}.\n'
                result += f'Значение: {self.date}\n'
                result += f'Полученный факт: {Translator(to_lang="ru").translate(self.fact["text"].title())}.\n'
                result += f'Добавил заметку: {"Да" if self.check_note else "Нет"}\n'
                result += f'Сохранил в базу данных: {"Да" if self.check_save else "Нет"}\n'
                result += f'-----------------------------------------------------------------------------------------\n'
                logs.write(result)

            elif self.info[1] == 'Получить рандомный факт':
                if self.received_info[1] == 'year' or self.received_info[1] == 'math' or self.received_info[1] == 'trivia':
                    result += f'Пользователь: {self.username}\n'
                    result += f'Выбраный тип факта: {self.info[1]}.\n'
                    result += f'Значение: {self.fact["number"]}\n'
                    result += f'Полученный факт: {Translator(to_lang="ru").translate(self.fact["text"].title())}.\n'
                    result += f'Добавил заметку: {"Да" if self.check_note else "Нет"}\n'
                    result += f'Сохранил в базу данных: {"Да" if self.check_save else "Нет"}\n'
                    result += f'-----------------------------------------------------------------------------------------\n'
                    logs.write(result)

                elif self.received_info[1] == 'date':
                    result += f'Пользователь: {self.username}\n'
                    result += f'Выбраный тип факта: {self.info[1]}.\n'
                    result += f'Значение: {self.fact["year"]}\n'
                    result += f'Полученный факт: {Translator(to_lang="ru").translate(self.fact["text"].title())}.\n'
                    result += f'Добавил заметку: {"Да" if self.check_note else "Нет"}\n'
                    result += f'Сохранил в базу данных: {"Да" if self.check_save else "Нет"}\n'
                    result += f'-----------------------------------------------------------------------------------------\n'
                    logs.write(result)

    def save(self):
        self.check_save = True
        con = sqlite3.connect("users.sql")
        cur = con.cursor()

        original = """INSERT INTO information(user, choice, data, result) VALUES (?, ?, ?, ?);"""

        if (self.info[1] == 'Получить мудреный факт о числе' or self.info[1] == 'Получить примитивный факт о числе'
                or self.info[1] == 'Получить факт о годе'):
            cur.execute(original, (str(self.username), str(self.info[1]), str(self.info[2]),
                                   str(Translator(to_lang='ru').translate(self.fact['text'].title()))))

        elif self.info[1] == 'Получить факт о дате':
            cur.execute(original, (str(self.username), str(self.info[1]), str(self.date),
                                   str(Translator(to_lang='ru').translate(self.fact['text'].title()))))

        elif self.info[1] == 'Получить рандомный факт':
            if self.received_info[1] == 'year' or self.received_info[1] == 'math' or self.received_info[1] == 'trivia':
                cur.execute(original, (str(self.username), str(self.info[1]), str(self.fact["number"]),
                            str(Translator(to_lang='ru').translate(self.fact['text'].title()))))

            elif self.received_info[1] == 'date':
                cur.execute(original, (str(self.username), str(self.info[1]), str(self.fact["year"]),
                            str(Translator(to_lang='ru').translate(self.fact['text'].title()))))
        con.commit()
        con.close()

        self.del_acc_error1.setText('Успешно сохранено в БД.')
        self.note_btn.setText('Добавить заметку')

    def add_note(self):
        if self.check_save:
            self.check_note = True
            if (self.info[1] == 'Получить мудреный факт о числе' or self.info[1] == 'Получить примитивный факт о числе'
                    or self.info[1] == 'Получить факт о годе'):
                self.note_text = Note(self, str(self.username), str(self.info[1]), str(self.info[2]),
                                      str(Translator(to_lang='ru').translate(self.fact['text'].title())))
                self.note_text.show()

            elif self.info[1] == 'Получить факт о дате':
                self.note_text = Note(self, str(self.username), str(self.info[1]), str(self.date),
                                      str(Translator(to_lang='ru').translate(self.fact['text'].title())))
                self.note_text.show()

            elif self.info[1] == 'Получить рандомный факт':
                if (self.received_info[1] == 'year' or self.received_info[1] == 'math'
                        or self.received_info[1] == 'trivia'):
                    self.note_text = Note(self, str(self.username), str(self.info[1]), int(self.fact["number"]),
                                          str(Translator(to_lang='ru').translate(self.fact['text'].title())))
                    self.note_text.show()

                elif self.received_info[1] == 'date':
                    self.note_text = Note(self, str(self.username), str(self.info[1]), int(self.fact["year"]),
                                          str(Translator(to_lang='ru').translate(self.fact['text'].title())))
                    self.note_text.show()

            self.del_acc_error2.setText('Заметка добавлена успешно.')
            self.note_btn.setText('Изменить заметку')
        else:
            self.del_acc_error2.setText('Заметку можно добавить после сохранения в БД.')

    def requests_form(self):
        from request_selection import Requests
        con = sqlite3.connect("users.sql")
        cur = con.cursor()

        cur.execute("""DELETE FROM information WHERE choice = ''""")

        name = """INSERT INTO information(user, choice, data, result) VALUES (?, ?, ?, ?);"""
        cur.execute(name, (self.username, '', '', ''))

        con.commit()
        con.close()

        self.write_logs()

        self.to_requests = Requests(self)
        self.to_requests.show()
        self.close()

    def action_form(self):
        from actions import Actions

        con = sqlite3.connect("users.sql")
        cur = con.cursor()

        cur.execute("""DELETE FROM information WHERE choice = ''""")

        name = """INSERT INTO information(user, choice, data, result) VALUES (?, ?, ?, ?);"""
        cur.execute(name, (self.username, '', '', ''))

        con.commit()
        con.close()

        self.write_logs()

        self.to_action = Actions(self)
        self.to_action.show()
        self.close()

    def login_form(self):
        from login_method import Login

        self.write_logs()

        self.to_login = Login(self)
        self.to_login.show()
        self.close()

    def cancellation(self):
        self.write_logs()

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Facts()
    ex.show()
    sys.exit(app.exec())