from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton



class LayoutTest(QWidget):

    def __init__(self,what):
        super().__init__()
        print("In LayOut 생성자")
        if what == 'absol':
            print('IF ==tooltip Step IN')
            self.absolute_layout()
        elif what == 'b':
            print('IF ==status Step IN')
        elif what == 'c':
            print('IF ==setStyle Step IN')
            # self.designStyle()



    def absolute_layout(self):

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()