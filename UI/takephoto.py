# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'takephoto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request as ur
import cv2
import numpy as np
import keyboard

url='http://192.168.1.1:8080/photoaf.jpg'


class Ui_takephotowindow(object):
    
    
    def goback(self):
        try:
            
            from inputimage import Ui_inputimage
            self.window=QtWidgets.QMainWindow()
            self.ui2= Ui_inputimage()
            self.ui2.setupUi(self.window)
            takephotowindow.close()
            self.window.show()
        except Exception as ex:
            print(ex)


    def clickpic(self):
        
        try:
            

             img_resp = ur.urlopen(url)
             image = np.asarray(bytearray(img_resp.read()), dtype="uint8")
             frame = cv2.imdecode(image, cv2.IMREAD_COLOR)
             
             img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
             pix = QtGui.QPixmap.fromImage(img)
             self.imgdisplay.setPixmap(pix)
             cv2.imwrite("./inputimg/"+"input.png",frame)
            # cv2.waitKey(0)
                   
            
        except Exception as ex:
            print(ex)

    def proceed(self):

        try:
            
            from recognizer import Ui_MainWindow
            self.window=QtWidgets.QMainWindow()
            self.ui2= Ui_MainWindow()
            self.ui2.setupUi(self.window)
            takephotowindow.close()
            self.window.show()
        except Exception as ex:
            print(ex)



    
    def setupUi(self, takephotowindow):
        takephotowindow.setObjectName("takephotowindow")
        takephotowindow.resize(648, 823)
        takephotowindow.setStyleSheet("*\n"
"{\n"
"    background:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(takephotowindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.base = QtWidgets.QFrame(self.centralwidget)
        self.base.setMinimumSize(QtCore.QSize(40, 100))
        self.base.setStyleSheet("#base\n"
"{\n"
"  border: 1px solid orange;\n"
"border-radius:20px   10px 20px ;\n"
"    \n"
"\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"\n"
"    background:url(:/bgrounds/bgcat.jpg);\n"
"}")
        self.base.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.base.setFrameShadow(QtWidgets.QFrame.Raised)
        self.base.setObjectName("base")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.base)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.base)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.heading = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setStyleSheet("#heading\n"
"{\n"
"  color: white;\n"
"    background: rgba(209, 209, 209,0.3);\n"
"border-radius:5px;\n"
"\n"
"}")
        self.heading.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.heading.setObjectName("heading")
        self.verticalLayout_2.addWidget(self.heading)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.base)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.imgdisplay = QtWidgets.QLabel(self.frame_5)
        self.imgdisplay.setMinimumSize(QtCore.QSize(348, 169))
        self.imgdisplay.setMaximumSize(QtCore.QSize(700, 500))
        self.imgdisplay.setStyleSheet("QLabel\n"
"{\n"
" border: 1px solid white;\n"
"}\n"
"")
        self.imgdisplay.setText("")
        self.imgdisplay.setObjectName("imgdisplay")
        self.horizontalLayout_3.addWidget(self.imgdisplay)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.base)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.takephotobtn = QtWidgets.QPushButton(self.frame_3)
        self.takephotobtn.setMinimumSize(QtCore.QSize(300, 25))
        self.takephotobtn.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setItalic(True)
        self.takephotobtn.setFont(font)
        self.takephotobtn.setStyleSheet("QPushButton\n"
"{\n"
"  color:white;\n"
"background:rgb(228, 152, 0);\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:black;\n"
"background:rgba(228, 152, 0,0.5);\n"
"border-radius: 10px;\n"
"border: 2px solid orange;\n"
"}")
        self.takephotobtn.setObjectName("takephotobtn")
        self.horizontalLayout_2.addWidget(self.takephotobtn)
        self.verticalLayout.addWidget(self.frame_3)
        spacerItem = QtWidgets.QSpacerItem(0, 67, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.frame_4 = QtWidgets.QFrame(self.base)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(30, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backbtn = QtWidgets.QPushButton(self.frame_4)
        self.backbtn.setMinimumSize(QtCore.QSize(116, 35))
        self.backbtn.setMaximumSize(QtCore.QSize(167, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.backbtn.setFont(font)
        self.backbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backbtn.setStyleSheet("#backbtn\n"
"{\n"
"   background:rgb(126, 0, 0) ;\n"
"    \n"
"color: white;\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"#backbtn:hover\n"
"{\n"
"   \n"
"   background: rgb(175, 0, 0);\n"
"\n"
"border-radius:10px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bgrounds/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backbtn.setIcon(icon)
        self.backbtn.setIconSize(QtCore.QSize(35, 35))
        self.backbtn.setObjectName("backbtn")
        self.horizontalLayout.addWidget(self.backbtn)
        self.proceedbtn = QtWidgets.QPushButton(self.frame_4)
        self.proceedbtn.setMinimumSize(QtCore.QSize(116, 35))
        self.proceedbtn.setMaximumSize(QtCore.QSize(167, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.proceedbtn.setFont(font)
        self.proceedbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.proceedbtn.setStyleSheet("#proceedbtn\n"
"{\n"
"   \n"
"    background-color: rgb(0, 170, 127);\n"
"border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"#proceedbtn:hover\n"
"{\n"
"\n"
"  border-radius:10px;\n"
"background-color: rgb(0, 170, 80)\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/bgrounds/proceed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.proceedbtn.setIcon(icon1)
        self.proceedbtn.setIconSize(QtCore.QSize(35, 35))
        self.proceedbtn.setObjectName("proceedbtn")
        self.horizontalLayout.addWidget(self.proceedbtn)
        self.verticalLayout.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.base, 0, 0, 1, 1)
        takephotowindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(takephotowindow)
        self.statusbar.setObjectName("statusbar")
        takephotowindow.setStatusBar(self.statusbar)

        self.retranslateUi(takephotowindow)
        QtCore.QMetaObject.connectSlotsByName(takephotowindow)


        self.backbtn.clicked.connect(self.goback)
        self.takephotobtn.clicked.connect(self.clickpic)
        self.proceedbtn.clicked.connect(self.proceed)


    def retranslateUi(self, takephotowindow):
        _translate = QtCore.QCoreApplication.translate
        takephotowindow.setWindowTitle(_translate("takephotowindow", "MainWindow"))
        self.heading.setText(_translate("takephotowindow", "Take Photo"))
        self.takephotobtn.setText(_translate("takephotowindow", "Take Photo"))
        self.backbtn.setText(_translate("takephotowindow", "Back"))
        self.proceedbtn.setText(_translate("takephotowindow", "Proceed"))

import bg_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    takephotowindow = QtWidgets.QMainWindow()
    ui = Ui_takephotowindow()
    ui.setupUi(takephotowindow)
    takephotowindow.show()
    sys.exit(app.exec_())

