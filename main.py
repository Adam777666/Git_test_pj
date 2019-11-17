import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MainFormlo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_wind = MainFormlo()
    main_wind.show()
    sys.exit(app.exec())
