# import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, QDesktopWidget,qApp
# from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QIcon
import Common_UI as commonUI

class ToolGogo(QWidget):
    def __init__(self, whatwant):
        super().__init__()
        self.what = whatwant
        if self.what == 'tooltip':
            print('IF ==tooltip Step IN')
            self.tooltipfunc()
        elif self.what == 'staus':
            print('IF ==status Step IN')
        elif self.what == 'stylego':
            print('IF ==setStyle Step IN')
            self.designStyle()


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
        # self.center()
        # commonUI.center_Desktop(self)
        CommonModule.center_Desktop(self)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        # self.center()
        CommonModule.center_Desktop(self)
        self.move(qr.topLeft())

    def designStyle(self):

        from PyQt5.QtWidgets import QLabel, QVBoxLayout
        print("In DesignStyle func")

        lbl_red = QLabel('Red')
        lbl_green= QLabel('Green')
        lbl_blue = QLabel('Blue')

        lbl_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 6px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px")

        lbl_green.setStyleSheet("color: green;"
                              "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 4px;"
                               "border-color: #1E90FF;"
                                "border-radius: 6px")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)
        self.setLayout(vbox)
        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()

class FromMainWindows(QMainWindow):
    def __init__(self, whatwant):
        super().__init__()
        self.what = whatwant
        if self.what == 'staus':
            print('IF ==tooltip Step IN')
            self.StatusGogo()
        elif self.what == 'menugo':
            print('IF ==status Step IN')
            self.MenubarGoGo()
        elif self.what == 'toolbargo':
            print('IF ==toolbar Step IN')
            self.maketoolbar()


    def StatusGogo(self):
        print('Step in ShowStatus')
        self.statusBar().showMessage('Ready')

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QMainWindows</b> ToolTips')
        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def MenubarGoGo(self):
        print('Step in MenubarGoGo')
        menulist = ['&File', '&View', '&Option']
        '''
            file을 눌렀을때... 아래 하단에 세부 메뉴 뜨게 만드는 것...
        '''
        exitAction = QAction(QIcon('./resources/Icon/exit.png'), 'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Appication')
        exitAction.triggered.connect(qApp.quit)

        openAction = QAction(QIcon('./resources/Icon/exit.png'), 'Open',self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open File')
        # openAction.triggered.connect(qApp.file)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu.addAction(openAction)

        viewmenu = menubar.addMenu(menulist[1])
        optionmenu = menubar.addMenu(menulist[2])
        ''' TEST'''



        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 500, 200)
        self.show()
    '''구조 자체는 메뉴바와 유사함'''
    def maketoolbar(self):
        exitAction = QAction(QIcon('./resources/Icon/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        # self.center()
        CommonModule.center_Desktop(self)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



class   CommonModule(QWidget):
    def __init__(self):
        super().__init__()

    def center_Desktop(self):
        print('Common Module IN')
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
