import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QComboBox

from data_input import Input


class Requests(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Выбор запроса')

        self.choose = QLabel(self)
        self.choose.resize(55, 20)
        self.choose.move(10, 10)
        self.choose.setText('Выберите:')

        self.requests = QComboBox(self)
        self.requests.move(10, 40)
        self.requests.addItems(['Получить факт о дате', 'Получить мудреный факт о числе', 'Получить рандомный факт',
                                'Получить примитивный факт о числе', 'Получить факт о годе'])

        self.ok_btn = QPushButton('ОК', self)
        self.ok_btn.resize(30, 30)
        self.ok_btn.move(240, 30)
        self.ok_btn.clicked.connect(self.ok)

        self.cancel_btn = QPushButton('Закрыть', self)
        self.cancel_btn.resize(55, 30)
        self.cancel_btn.move(240, 70)
        self.cancel_btn.clicked.connect(self.cancellation)

    def ok(self):
        self.request = Input(self, self.requests.currentText())
        self.request.show()
        self.close()

    def cancellation(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Requests()
    ex.show()
    sys.exit(app.exec())