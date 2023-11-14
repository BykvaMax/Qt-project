import sqlite3
import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QLabel, QWidget, QTextEdit


class Note(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.info = args
        self.setGeometry(750, 360, 310, 150)
        self.setWindowTitle('Заметка')
        self.note_content = ''

        self.note_txt = QLabel(self)
        self.note_txt.resize(300, 20)
        self.note_txt.move(10, 10)
        self.note_txt.setText('Введите содержание заметки:')

        self.input_note = QTextEdit(self)
        self.input_note.resize(250, 100)
        self.input_note.move(10, 40)

        self.ok_btn = QPushButton('ОК', self)
        self.ok_btn.resize(30, 30)
        self.ok_btn.move(270, 110)
        self.ok_btn.clicked.connect(self.give_note)

    def give_note(self):
        self.wrong_note = self.input_note.toPlainText().split()
        self.correct_note = ''
        for i in self.wrong_note:
            self.correct_note += f'{i} '

        con = sqlite3.connect("users.sql")
        cur = con.cursor()
        original = """UPDATE information SET note = ? WHERE user = ? AND choice = ? AND data = ? AND result = ?"""

        cur.execute(original, (self.correct_note, self.info[1], self.info[2], str(self.info[3]), self.info[4]))

        con.commit()
        con.close()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Note()
    ex.show()
    sys.exit(app.exec())