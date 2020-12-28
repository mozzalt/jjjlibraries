# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, QDesktopWidget,qApp

from PyQt5.QtWidgets import QDesktopWidget,QWidget
# from PyQt5.QtGui import QFont, QIcon



class   CommonModule(QWidget):
    def __init__(self):
        print("Common 생성자")
        super().__init__()
        self.center_Desktop()

    def center_Desktop(self):
        print('Common Module IN')
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())