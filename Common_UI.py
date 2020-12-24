# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, QDesktopWidget,qApp

from PyQt5.QtWidgets import QDesktopWidget
# from PyQt5.QtGui import QFont, QIcon



class   CommonModule():
    def __init__(self):
        super().__init__()

    def center_Desktop(self):
        print('Common Module IN')
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())