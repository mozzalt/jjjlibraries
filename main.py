import sys
# from PyQt5.QtWidgets import QApplication,  QWidget
from PyQt5.QtWidgets import *
import  Instance_new_windows as popwin
import  Icon_into_application as icongo
import  quit_BTN as qbtn
import  qtTestfunc as qtool
import Layout_Test as laytest
import Widget_Test as wTest
import get_exif_from_Img as EXIF
# FromMainWindows
# from qtTestfunc import FromMainWindows, ToolGogo




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # ex = popwin.MyApp()
    #ex = icongo.Myapp()
    #ex = qbtn.QuitBTN()
    #ex = qTetTool.QuitBTN('quitbtn')
    # ex = qtool.ToolGogo('tooltip')
    # ex = qtool.FromMainWindows('menugo')
    # ex = qtool.FromMainWindows('toolbargo')
    #  ex = qtool.ToolGogo('stylego')
    # ex = laytest.LayoutTest('gridlay')
    # ex = laytest.LayoutTest('boxlay')
    # ex = laytest.LayoutTest('absol')
    # ex = wTest.WidgetBasic('lbltest')
    # ex = wTest.WidgetBasic('cbtest')
    # ex = wTest.WidgetBasic('rdbtest')
    # ex = wTest.WidgetBasic('combotest')
    # ex = wTest.WidgetBasic('linedit')
    # ex = wTest.WidgetBasic('progress')
    # gFileInfo = ("File Name", "Shape", "Size", "Date", "Entropy", "Channel", "Exif", "GPS", "Stat")
    # print(len(gFileInfo))   # ...." " 갯수인 9개가 출력됨
    # ex = wTest.WidgetBasic('slide')
    ex = EXIF.Get_Exif_from_Img()


    sys.exit(app.exec_())

