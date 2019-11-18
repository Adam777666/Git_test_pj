import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import random


class MainFormlo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setWindowTitle('Кругляжки')
        self.setWindowIcon(QIcon('ping.png'))
        self.a = 0
        self.px = 0
        self.kryg_But.clicked.connect(self.creator)

    def creator(self):
        btn = QPushButton(self)
        self.giv_random2()
        btn.resize(self.a, self.a)
        btn.move(self.giv_random()[0], self.giv_random()[2])
        btn.setStyleSheet(
            f'''background-color: rgb({self.giv_random()[1]}, {self.giv_random()[1]}, {self.giv_random()[1]});
border-radius: {self.px}px;
border-style: solid;
border-width:5px;
border-color: black;''')
        btn.show()

    def giv_random(self):
        return random.randrange(0, 559), random.randrange(0, 255), random.randrange(10, 509)

    def giv_random2(self):
        self.lol_staf = (31, 41, 51, 61, 71, 81, 91)
        self.a = random.choice(self.lol_staf)
        if self.a == 31:
            self.px = 15
        if self.a == 41:
            self.px = 20
        if self.a == 51:
            self.px = 25
        if self.a == 61:
            self.px = 30
        if self.a == 71:
            self.px = 35
        if self.a == 81:
            self.px = 40
        if self.a == 91:
            self.px = 45


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_wind = MainFormlo()
    main_wind.show()
    sys.exit(app.exec())
