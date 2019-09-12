# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploadimage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import cv2 

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QFileDialog,QApplication,QWidget
from PyQt5.QtGui import QPixmap


class Ui_uploadimgwindow(object):

    def goback(self):
        try:
                from inputimage import Ui_inputimage
                uploadimgwindow = QtWidgets.QMainWindow()
                ui = Ui_uploadimgwindow()
                ui.setupUi(uploadimgwindow)
                
                self.window=QtWidgets.QMainWindow()
                self.ui2= Ui_inputimage()
                self.ui2.setupUi(self.window)
                uploadimgwindow.close()
               
                self.window.show()
        except Exception as ex:
            print(ex)
        
    def getImage(self):

        filtr = "Images (*.png *.jpg)"
        #print(QtCore.QDir.rootPath())
        try:
                obj= QtWidgets.QWidget() 
                fileName, _ = QtWidgets.QFileDialog.getOpenFileName(obj, 'Single File', QtCore.QDir.rootPath() , '*.jpeg *.png *.jpg')
                imagePath = fileName
                pixmap = QPixmap(imagePath)
                
                self.imgdisplay.setPixmap(pixmap)
                obj.resize(pixmap.width(), pixmap.height())
                img = cv2.imread(imagePath)
                cv2.imwrite("./inputimg/"+"input.png",img)

        except  Exception as ex:
            print(ex)
            
    def proceed(self):

            try:
                
                from recognizer import Ui_MainWindow
                self.window=QtWidgets.QMainWindow()
                self.ui2= Ui_MainWindow()
                self.ui2.setupUi(self.window)
                #uploadimgwindow.close()
                self.window.show()
            except Exception as ex:
                print(ex)   
         
        
        



    
    def setupUi(self, uploadimgwindow):
        uploadimgwindow.setObjectName("uploadimgwindow")
        uploadimgwindow.resize(648, 823)
        uploadimgwindow.setStyleSheet("*\n"
"{\n"
"    background:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(uploadimgwindow)
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
        self.imgdisplay.setMaximumSize(QtCore.QSize(1000, 800))
        self.imgdisplay.setStyleSheet("QLabel\n"
"{\n"
"   border:1px solid white;\n"
"}")
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
        self.chooseimgbtn = QtWidgets.QPushButton(self.frame_3)
        self.chooseimgbtn.setMinimumSize(QtCore.QSize(300, 25))
        self.chooseimgbtn.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.chooseimgbtn.setFont(font)
        self.chooseimgbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chooseimgbtn.setStyleSheet("QPushButton\n"
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
        self.chooseimgbtn.setObjectName("chooseimgbtn")
        self.horizontalLayout_2.addWidget(self.chooseimgbtn)
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
        uploadimgwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(uploadimgwindow)
        self.statusbar.setObjectName("statusbar")
        uploadimgwindow.setStatusBar(self.statusbar)

        self.retranslateUi(uploadimgwindow)
        QtCore.QMetaObject.connectSlotsByName(uploadimgwindow)

        self.backbtn.clicked.connect(self.goback)
        self.chooseimgbtn.clicked.connect(self.getImage)
        self.proceedbtn.clicked.connect(self.proceed)



    def retranslateUi(self, uploadimgwindow):
        _translate = QtCore.QCoreApplication.translate
        uploadimgwindow.setWindowTitle(_translate("uploadimgwindow", "MainWindow"))
        self.heading.setText(_translate("uploadimgwindow", "Upload Image"))
        self.chooseimgbtn.setText(_translate("uploadimgwindow", "Choose Image"))
        self.backbtn.setText(_translate("uploadimgwindow", "Back"))
        self.proceedbtn.setText(_translate("uploadimgwindow", "Proceed"))

import bg_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uploadimgwindow = QtWidgets.QMainWindow()
    ui = Ui_uploadimgwindow()
    ui.setupUi(uploadimgwindow)
    uploadimgwindow.show()
    sys.exit(app.exec_())

