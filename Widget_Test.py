from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtCore import Qt
import Common_UI as comUI

class WidgetBasic(QWidget):
    def __init__(self,what):
        super().__init__()

        if what=='btntest':
            self.pushbtn_test()
        elif what == 'lbltest':
            self.label_test()
        elif what == 'cbtest':
            self.checkbox_test()
        elif what == 'rdbtest':
            self.radio_btn_test()
        elif what == 'combotest':
            self.combo_test()
        elif what == 'linedit':
            self.line_edit_test()
        elif what == 'progress':
            self.progress_test()
        elif what == 'slide':
            self.slide_digal_test()
        elif what == 'split':
            self.split_test()
        elif what == 'groupbox':
            self.group_box_test()



    def pushbtn_test(self):
        from PyQt5.QtWidgets import QPushButton, QVBoxLayout
        '''Button1이 쓰여질 문구이고 &는 단축키 활성화, & 바로 뒷문자가 Alt+ 해당문자, self는 버튼을 품을 Parents'''
        btn1 = QPushButton('Button&1',self)
        '''setCheckable()을 True로 설정해주면, 선택되거나 선택되지 않은 상태를 유지할 수 있게 됩니다.'''
        btn1.setCheckable(True)
        '''toggle() 메서드를 호출하면 버튼의 상태가 바뀌게 됩니다. 따라서 이 버튼은 프로그램이 시작될 때 선택되어 있습니다.'''
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        '''setEnabled()를 False로 설정하면, 버튼을 사용할 수 없게 됩니다'''
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)



        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        # comUI.CommonModule()
        self.show()

    def label_test(self):
        from PyQt5.QtWidgets import QLabel, QVBoxLayout
        from PyQt5.QtCore   import Qt
        label1 = QLabel('First Label', self)
        '''Qt.AlignCenter로 설정해주면 수평, 수직 방향 모두 가운데 위치'''
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('Second Label', self)
        '''수직 방향으로만 가운데 (Qt.AlignVCenter)로 설정해줍니다.'''
        label2.setAlignment(Qt.AlignVCenter)

        font1 = label1.font()
        font1.setPointSize(20)

        '''폰트의 크기를 설정하지 않았기 때문에 디폴트 크기인 13으로 설정'''
        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 600, 400)
        # comUI.CommonModule()
        self.show()

    def checkbox_test(self):

        self.cb = QCheckBox('Cehcked',self)
        self.cb.move(130,130)

        # cb.setAlignment(Qt.AlignCenter)
        self.cb.toggle()
        self.cb.stateChanged.connect(self.changeTitle)

        # self.chage_TXT(cb)
        '''
        if cb.stateChanged.connect(self.changeTitle)==1:
            print('Cehcked')
            cb.setText('Checked')
        elif cb.stateChanged.connect(self.changeTitle)==0:
            print('UnCehcked')
            cb.setText('UnChecked')
        '''
        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 600, 400)
        # comUI.CommonModule()
        self.show()

    def changeTitle(self, cbstate):

        if cbstate == Qt.Checked:
            print('Cehcked----')
            self.setWindowTitle('QCheckBox')
            ''' 위 함수에서 정의한 cb를 못 가지고 오네...'''
            ''' 아... 해당 변수를 self.XX 로 선언하면 가져올 수 있네...'''
            self.cb.setText('Checked')
            self.cb.adjustSize()



        else:
            print('UnCehcked----')
            self.setWindowTitle(' ')
            self.cb.setText('UnChecked')
            self.cb.adjustSize()

    def chage_TXT(self,jjjcb):
        print('In Change_TXT Func')
        jjjcb.setText('ttt')
        '''
        state=1
        if state == 1:
            print('State 1')
        else :
            print('State not 1')
        '''

    def radio_btn_test(self):
        from PyQt5.QtWidgets import QRadioButton
        rbtn1  = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()

    def combo_test(self):
        from PyQt5.QtWidgets import QLabel, QComboBox
        self.label_from_combo = QLabel('Label from Combo',self)
        self.label_from_combo.move(100,300)
        cb1=QComboBox(self)


        cb1.addItem('Opqtion1')
        cb1.addItem('Opqtion2')
        cb1.addItem('Opqtion3')
        cb1.addItem('Opqtion4')
        cb1.move(150,100)

        cb1.activated[str].connect(self.combochage)



        # self.label_combo('JJJ')
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('QRadioButton')
        self.show()

    def combochage(self,combo_txt):
        self.label_from_combo.setText(combo_txt)
        self.label_from_combo.adjustSize()



    def line_edit_test(self):
        from PyQt5.QtWidgets import QLabel, QLineEdit

        self.label_from_lineedit=QLabel('JJJ',self)
        self.label_from_lineedit.move(200,100)

        lines=QLineEdit(self)
        lines.move(200,150)
        lines.setEchoMode(QLineEdit.Password)
        lines.textChanged[str].connect(self.changed_lineEdit)
        # lines.returnPressed.connect(self.changed_lineEdit)



        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Qline_edit_test')
        self.show()

    def changed_lineEdit(self, line_text):
        self.label_from_lineedit.setText(line_text)
        self.label_from_lineedit.adjustSize()

    def progress_test(self):
        from PyQt5.QtWidgets import QPushButton, QProgressBar
        from PyQt5.QtCore import QBasicTimer

        self.pbar=QProgressBar(self)
        self.pbar.setGeometry(50,50,300,30)

        self.startbtn=QPushButton('Start',self)
        self.startbtn.move(50,100)
        self.startbtn.clicked.connect(self.goProgressbar)

        self.resetbtn=QPushButton('Reset',self)
        self.resetbtn.move(200,100)
        self.resetbtn.clicked.connect(self.resetProgressbar)

        self.timer = QBasicTimer()
        self.step =0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300,300,600,400)
        self.show()

    ''' Important ... progressbar Show...'''
    def timerEvent(self, e):
        print('timeEvent is Called')
        if self.step >=100:
            self.timer.stop()
            self.startbtn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def goProgressbar(self):
        print('In goProgressbar func')
        if self.timer.isActive():
            print('Timer is Active')
            self.timer.stop()
            self.startbtn.setText('Start')
        else :
            print('Timer is DeActive')
            self.timer.start(100,self)
            self.startbtn.setText('Stop')

    def resetProgressbar(self):
        # self.timer.stop()
        self.timer.start(100,self)
        self.step = 0
        self.startbtn.setText('Stop')


    def slide_digal_test(self):
        from PyQt5.QtWidgets import QSlider, QPushButton, QDial
        from PyQt5.QtCore import Qt

        self.slider = QSlider(Qt.Horizontal,self)
        self.slider.move(100,100)
        self.slider.setRange(0,300)
        self.slider.setSingleStep(10)

        self.dial = QDial(self)
        self.dial.move(100,200)
        self.dial.setRange(0, 300)

        btn = QPushButton('Default',self)
        btn.move(105,340)
        btn.clicked.connect(self.set_def_dial_slide)

        ''' JJJ Tip... Connect에... 함수연결이아닌 직접 값을 Assign 해서 해결하네...'''
        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)



        self.setWindowTitle('Slide and Dial')
        self.setGeometry(300,300,600,400)
        self.show()

    def set_def_dial_slide(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


    def split_test(self):

        from PyQt5.QtWidgets import QHBoxLayout, QFrame, QSplitter
        from PyQt5.QtCore import Qt

        hbox = QHBoxLayout()

        ''' 4개의 Frame으로 만들기...'''

        top = QFrame()
        top.setFrameShape(QFrame.Box)


        midleft =  QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)
        midleft.adjustSize()
        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)
        midright.adjustSize()
        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        '''
        hbox.addWidget(top)
        hbox.addWidget(midleft)
        hbox.addWidget(midright)
        hbox.addWidget(bottom)
        hbox.addWidget(splitter1)
        '''
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Split Test Gogo')
        self.show()


    def group_box_test(self):
        from PyQt5.QtWidgets import (QGroupBox, QRadioButton, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout)

        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)

        grid.addWidget(self.createPushButtonGroup(), 1, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('group_box_test Test Gogo')
        self.show()


    def createFirstExclusiveGroup(self):
        from PyQt5.QtWidgets import QGroupBox, QRadioButton, QVBoxLayout
        groupbox = QGroupBox('(0,0)Exclusive Radio Buttons')

        radio1 = QRadioButton('Radio 1')
        radio2 = QRadioButton('Radio 2')
        radio3 = QRadioButton('Radio 3')
        radio4 = QRadioButton('Radio 4')

        radio1.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(radio4)

        groupbox.setLayout(vbox)
        return groupbox

    def createSecondExclusiveGroup(self):
        from PyQt5.QtWidgets import QGroupBox, QRadioButton, QVBoxLayout
        groupbox = QGroupBox('(1,0)Exclusive Radio Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        checkbox = QCheckBox('Independent Checkbox')
        checkbox.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(8)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
        groupbox = QGroupBox('(0,1)Non-Exclusive Checkboxes')
        groupbox.setFlat(True)

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self):
        from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QMenu
        groupbox = QGroupBox('Push Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        pushbutton = QPushButton('Normal Button')
        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True)
        popupbutton = QPushButton('Popup Button')
        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox