from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton



class LayoutTest(QWidget):

    def __init__(self,what):
        super().__init__()
        print("In LayOut 생성자")
        if what == 'absol':
            print('IF ==absolute__layout Step IN')
            self.absolute_layout()
        elif what == 'boxlay':
            print('IF ==box__layout Step IN')
            self.box_layout()
        elif what == 'gridlay':
            print('IF ==gridlay Step IN')
            self.grid_layout()



    def absolute_layout(self):

        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)
        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def box_layout(self):
        from PyQt5.QtWidgets import  QPushButton, QHBoxLayout, QVBoxLayout
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(10)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def grid_layout(self):
        from PyQt5.QtWidgets import ( QGridLayout, QLabel, QLineEdit, QTextEdit)
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)



        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
