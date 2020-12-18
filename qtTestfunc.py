import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class   toolgogo(QWidget):

    def __init__(self,whatwant):
        super().__init__()
        self.what = whatwant

        if self.what == 'tooltip':
            print('IF ==1 Step IN')
            self.tooltipfunc()
        elif self.what == 'what':
            print('Next Time gogo')


    def tooltipfunc(self):
        print('Setp In What Func')

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()
