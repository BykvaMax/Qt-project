import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap

from login_method import Login


class Introduction(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 330)
        self.setWindowTitle('Вступление')

        self.welcome_txt = QLabel(self)
        self.welcome_txt.resize(300, 20)
        self.welcome_txt.move(150, 10)
        self.welcome_txt.setText('Добро пожаловать в приложение:')

        self.title = QLabel(self)
        self.title.resize(300, 20)
        self.title.move(200, 30)
        self.title.setText('Факты о цифрах!')

        self.text1 = QLabel(self)
        self.text1.resize(300, 20)
        self.text1.move(10, 80)
        self.text1.setText('Здесь вы можете:')

        self.text2 = QLabel(self)
        self.text2.resize(300, 20)
        self.text2.move(10, 110)
        self.text2.setText('1. Узнать факты о датах.')

        self.text2 = QLabel(self)
        self.text2.resize(300, 20)
        self.text2.move(10, 140)
        self.text2.setText('2. Узнать факты о годах.')

        self.text3 = QLabel(self)
        self.text3.resize(300, 20)
        self.text3.move(10, 170)
        self.text3.setText('3. Узнать факты о числах.')

        self.text4 = QLabel(self)
        self.text4.resize(300, 20)
        self.text4.move(10, 200)
        self.text4.setText('4. Узнать рандомные факты.')

        self.text5 = QLabel(self)
        self.text5.resize(300, 20)
        self.text5.move(10, 230)
        self.text5.setText('5. А также просто убить время.')

        self.image = 'numbers.webp'
        self.num_img = QPixmap(self.image)
        self.num_img = self.num_img.scaled(300, 250, Qt.KeepAspectRatio)

        self.numbers = QLabel(self)
        self.numbers.move(190, 60)
        self.numbers.setPixmap(self.num_img)

        self.start_btn = QPushButton('Начать', self)
        self.start_btn.resize(480, 30)
        self.start_btn.move(10, 290)
        self.start_btn.clicked.connect(self.start)

    def start(self):
        self.start = Login(self)
        self.start.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Introduction()
    ex.show()
    sys.exit(app.exec())