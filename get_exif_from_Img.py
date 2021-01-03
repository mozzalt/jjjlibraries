import os

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QGridLayout,
                             QFileDialog)
from PyQt5.QtCore import Qt, QObject, QDir, QUrl, QThreadPool, QTimer, QFile, QFileInfo

from PIL import Image, ExifTags, ImageStat
from PIL.ExifTags import TAGS, GPSTAGS


class Get_Exif_from_Img (QWidget):
    def __init__(self):
        super ().__init__ ()
        self.simple_UI ()
        # self.testForloop()
    '''
    def testForloop(self):
        test_list = ['one', 'two', 'three']
       
        for i in test_list:
            print(i)
        a = [(1, 2), (3, 4), (5, 6)]
        for (first, last) in a:
            print(first)
            # print("last  :" + last)
       

        for i in range(1,10):
            print(i)
    '''


    def simple_UI(self):
        # 전체 몸통....

        self.img_path = ''

        mainlayout = QVBoxLayout ()
        layout = QGridLayout ()
        # layout = QGridLayout ()
        img_label = QLabel ('Image PATH', self)
        # img_label.move(20,20)

        self.path_label = QLabel ()
        # self.path_label.move(20,130)

        self.path_txtBox = QLineEdit (self.img_path, self)
        # self.path_txtBox.move (130, 20)
        self.path_txtBox.adjustSize ()

        get_path_btn = QPushButton ('Get Path', self)
        # get_path_btn.move(20,50)
        get_path_btn.setCheckable (True)
        get_path_btn.clicked.connect (self.getImagepath)

        # layout.addWidget(img_label, 0, 0)
        layout.addWidget (img_label, 0, 0)
        layout.addWidget (self.path_label, 1, 0)
        layout.addWidget (self.path_txtBox, 0, 1)
        layout.addWidget (get_path_btn, 0, 2)

        # mainlayout.addWidget(layout)

        self.setLayout (layout)
        self.setWindowTitle ('EXIF Info of IMAGE')
        self.setGeometry (100, 100, 1000, 400)
        self.show ()

    def getImagepath(self):
        # dir = QFileDialog.getExistingDirectory(self, "Find Your Images", QDir.currentPath()
        fName = QFileDialog.getOpenFileName (self)  # , "Images", "*.jpg;*.png", )
        self.img_path = fName
        print (fName[0])
        self.path_txtBox.setText (fName[0])
        # self.path_txtBox.setText ('jjjj')
        self.path_label.setText (fName[0])
        self.get_exif_of_file (fName[0])

    def get_exif_of_file(self, file):
        im = Image.open (file)
        return self.get_exif(im)

    def get_exif(self, im):
        try:
            # exif = im._getexif ()
            exif = im.getexif()
        except AttributeError:
            print('EXCEPT')
            return {}
        if exif is None:
            print ("exif is NONE??")
            return {}

        exif_table = {}
        print ("for loop gogogo")

        for tag_id, value in exif.items():
            tag = TAGS.get (tag_id, tag_id)
            exif_table[tag] = value
            print(exif_table[tag])

        return exif_table

    def get_exif_string(self, im):
        return str (self.get_exif (im))