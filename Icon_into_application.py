# import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.iconInsert()

    def iconInsert(self):
        self.setWindowTitle('Icon Inserted')
        self.setWindowIcon(QIcon('./resources/Icon/web.png'))
        '''
        tt = QIcon("./resources/Icon/web.png")
        self.setWindowIcon(tt)
        '''
        self.setGeometry(300,300,600,200)
        self.show()
