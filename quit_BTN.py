import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class QuitBTN(QWidget):
    def __init__(self):
        super().__init__()
        self.quitbutton()

    def quitbutton(self):
        btn1 = QPushButton('Quit', self)
        btn1.move(50, 50)
        btn1.resize(btn1.sizeHint())
        # btn1.click().conn
        btn1.clicked.connect(QCoreApplication.instance().quit)
        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 500, 200)
        self.show()