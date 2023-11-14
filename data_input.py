import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

from fact import Facts


class Input(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.requeast = args[1]
        self.choice = ''
        if args[1] == 'Получить мудреный факт о числе' or args[1] == 'Получить примитивный факт о числе':
            self.choice = 'Число'
            self.setGeometry(300, 300, 300, 100)
            self.setWindowTitle('Ввод данных')

            self.data = QLabel(self)
            self.data.resize(130, 20)
            self.data.move(10, 10)
            self.data.setText('Введите любое число:')

            self.input_data = QLineEdit(self)
            self.input_data.adjustSize()
            self.input_data.move(140, 10)

            self.error = QLabel(self)
            self.error.resize(150, 20)
            self.error.move(10, 50)

            self.ok_btn = QPushButton('ОК', self)
            self.ok_btn.resize(30, 30)
            self.ok_btn.move(190, 50)
            self.ok_btn.clicked.connect(self.confirmation)

            self.cancel_btn = QPushButton('Закрыть', self)
            self.cancel_btn.resize(55, 30)
            self.cancel_btn.move(240, 50)
            self.cancel_btn.clicked.connect(self.cancellation)

        elif args[1] == 'Получить факт о годе':
            self.choice = 'Год'
            self.setGeometry(300, 300, 300, 100)
            self.setWindowTitle('Ввод данных')

            self.data = QLabel(self)
            self.data.resize(130, 20)
            self.data.move(10, 10)
            self.data.setText('Введите год:')

            self.input_year = QLineEdit(self)
            self.input_year.adjustSize()
            self.input_year.move(140, 10)

            self.year_error = QLabel(self)
            self.year_error.resize(150, 20)
            self.year_error.move(10, 50)

            self.ok_btn = QPushButton('ОК', self)
            self.ok_btn.resize(30, 30)
            self.ok_btn.move(190, 50)
            self.ok_btn.clicked.connect(self.confirmation)

            self.cancel_btn = QPushButton('Закрыть', self)
            self.cancel_btn.resize(55, 30)
            self.cancel_btn.move(240, 50)
            self.cancel_btn.clicked.connect(self.cancellation)


        elif args[1] == 'Получить факт о дате':
            self.choice = 'Дата'
            self.setGeometry(300, 300, 300, 130)
            self.setWindowTitle('Ввод данных')

            self.month = QLabel(self)
            self.month.resize(100, 20)
            self.month.move(10, 10)
            self.month.setText('Введите месяц:')

            self.input_month = QLineEdit(self)
            self.input_month.resize(100, 20)
            self.input_month.move(100, 10)

            self.day = QLabel(self)
            self.day.resize(100, 20)
            self.day.move(10, 40)
            self.day.setText('Введите день:')

            self.input_day = QLineEdit(self)
            self.input_day.resize(100, 20)
            self.input_day.move(100, 40)

            self.month_error = QLabel(self)
            self.month_error.resize(150, 20)
            self.month_error.move(10, 70)

            self.day_error = QLabel(self)
            self.day_error.resize(150, 20)
            self.day_error.move(10, 100)

            self.ok_btn = QPushButton('ОК', self)
            self.ok_btn.resize(30, 30)
            self.ok_btn.move(190, 70)
            self.ok_btn.clicked.connect(self.confirmation)

            self.cancel_btn = QPushButton('Закрыть', self)
            self.cancel_btn.resize(55, 30)
            self.cancel_btn.move(240, 70)
            self.cancel_btn.clicked.connect(self.cancellation)

        elif args[1] == 'Получить рандомный факт':
            self.choice = 'Рандом'
            self.setGeometry(300, 300, 350, 160)
            self.setWindowTitle('Ввод данных')

            self.month = QLabel(self)
            self.month.resize(250, 20)
            self.month.move(10, 10)
            self.month.setText('Измените диапозон значений или нажмите ОК.')

            self.month = QLabel(self)
            self.month.resize(140, 20)
            self.month.move(10, 40)
            self.month.setText('Минимальное значение:')

            self.input_min = QLineEdit(self)
            self.input_min.setEnabled(True)
            self.input_min.resize(100, 20)
            self.input_min.move(150, 40)
            self.input_min.setText('-1000000')

            self.day = QLabel(self)
            self.day.resize(140, 20)
            self.day.move(10, 70)
            self.day.setText('Максимальное значение:')

            self.input_max = QLineEdit(self)
            self.input_max.setEnabled(True)
            self.input_max.resize(100, 20)
            self.input_max.move(150, 70)
            self.input_max.setText('1000000')

            self.min_error = QLabel(self)
            self.min_error.resize(250, 20)
            self.min_error.move(10, 100)

            self.max_error = QLabel(self)
            self.max_error.resize(250, 20)
            self.max_error.move(10, 130)

            self.ok_btn = QPushButton('ОК', self)
            self.ok_btn.resize(30, 30)
            self.ok_btn.move(250, 100)
            self.ok_btn.clicked.connect(self.confirmation)

            self.cancel_btn = QPushButton('Закрыть', self)
            self.cancel_btn.resize(55, 30)
            self.cancel_btn.move(290, 100)
            self.cancel_btn.clicked.connect(self.cancellation)



    def confirmation(self):
        equality = True
        check_month = False
        check_day = False
        call = False
        monthes = ['2', '4', '6', '9', '11', '1', '3', '5', '7', '8', '10', '12']

        if self.choice == 'Дата':
            try:
                int(self.input_month.text())
                check_month = True
                self.month_error.clear()
            except Exception:
                check_month = False
                self.month_error.setText('Вы ввели месяц неверно.')

            try:
                int(self.input_day.text())
                check_day = True
                self.day_error.clear()
            except Exception:
                check_day = False
                self.day_error.setText('Вы ввели день неверно.')

            if check_month and check_day:
                if int(self.input_month.text()) > 12 or int(self.input_month.text()) < 1:
                    self.month_error.setText('Вы ввели месяц неверно.')
                    check_month = False
                else:
                    self.month_error.clear()

                if int(self.input_day.text()) > 31 or int(self.input_day.text()) < 1:
                    self.day_error.setText('Вы ввели день неверно.')
                    check_day = False
                else:
                    self.day_error.clear()

                if check_month and check_day:
                    if int(self.input_day.text()) > 28 or int(self.input_day.text()) < 1 and self.input_month.text() == '2':
                        self.day_error.setText('Вы ввели день неверно.')
                    else:
                        if not call:
                            self.information = Facts(self, self.requeast, int(self.input_month.text()),
                                                     int(self.input_day.text()))
                            self.information.show()
                            self.close()
                            call = True

                    if (int(self.input_day.text()) > 30 or int(self.input_day.text()) < 1 and
                            self.input_month.text() in monthes[1:5]):
                        self.day_error.setText('Вы ввели день неверно.')
                    else:
                        if not call:
                            self.information = Facts(self, self.requeast, int(self.input_month.text()),
                                                     int(self.input_day.text()))
                            self.information.show()
                            self.close()
                            call = True

                    if (int(self.input_day.text()) > 31 or int(self.input_day.text()) < 1 and
                            self.input_month.text() in monthes[4:]):
                        self.day_error.setText('Вы ввели день неверно.')
                    else:
                        if not call:
                            self.day_error.clear()
                            self.information = Facts(self, self.requeast, int(self.input_month.text()),
                                                     int(self.input_day.text()))
                            self.information.show()
                            self.close()
                            call = True

        elif self.choice == 'Число':
            try:
                int(self.input_data.text())
                self.information = Facts(self, self.requeast, int(self.input_data.text()))
                self.information.show()
                self.close()
            except Exception:
                self.error.setText('Вы ввели число неверно.')

        elif self.choice == 'Год':
            year_check = False
            try:
                int(self.input_year.text())
                year = int(self.input_year.text())
                year_check = True
            except Exception:
                self.year_error.setText('Вы ввели год неверно.')

            if year_check:
                if year <= 2023:
                    self.information = Facts(self, self.requeast, year)
                    self.information.show()
                    self.close()
                else:
                    self.year_error.setText('Вы ввели год неверно.')

        elif self.choice == 'Рандом':
            try:
                int(self.input_min.text())
                self.min_error.clear()
                check = True
            except Exception:
                check = False
                self.min_error.setText('Вы ввели минимальное значение неверно.')

            try:
                int(self.input_max.text())
                self.max_error.clear()
            except Exception:
                    check = False
                    self.max_error.setText('Вы ввели максимальное значение неверно.')

            if check == True:
                if int(self.input_max.text()) < int(self.input_min.text()):
                    equality = False
                    self.min_error.setText('Вы ввели минимальное значение неверно.')
                    self.max_error.setText('Вы ввели максимальное значение неверно.')

            if equality == True and check == True:
                self.max_error.clear()
                self.information = Facts(self, self.requeast, int(self.input_min.text()),
                                         int(self.input_max.text()))
                self.information.show()
                self.close()

    def cancellation(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Input()
    ex.show()
    sys.exit(app.exec())