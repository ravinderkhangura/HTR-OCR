# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recognizer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):


    def goback(self):
        
        try:
            
            from inputimage import Ui_inputimage
            self.window=QtWidgets.QMainWindow()
            self.ui2= Ui_inputimage()
            self.ui2.setupUi(self.window)
            MainWindow.close()
            self.window.show()
        except Exception as ex:
            print(ex)
    def htr(self):
        try:
            import main
            recog,prob=main.main()
            self.label_3.setText(recog)
           

        except Exception as ex:
            print(ex)
    def ocr(self):
            try:
                import ocr
                recog=ocr.ocrfun()
                self.label_3.setText(recog)
               

            except Exception as ex:
                print(ex)
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
        MainWindow.setMinimumSize(QtCore.QSize(900, 800))
        MainWindow.setStyleSheet("#MainWindow\n"
"{\n"
"\n"
"    background-image: url(:/bgrounds/triangle.png);\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(800, 100))
        self.label.setMaximumSize(QtCore.QSize(800, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("*\n"
"{\n"
"\n"
"    border-radius: 20px;\n"
"    background-color: rgba(0, 0, 0,0.5);\n"
"    color: orange;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputdisplay = QtWidgets.QLabel(self.frame_5)
        self.inputdisplay.setMinimumSize(QtCore.QSize(500, 150))
        self.inputdisplay.setMaximumSize(QtCore.QSize(800, 200))
        self.inputdisplay.setStyleSheet("*\n"
"{\n"
"  border:1px solid green;\n"
"\n"
"    background-color: rgba(0,0, 0,0.5);\n"
"}")
        self.inputdisplay.setText("")
        self.inputdisplay.setObjectName("inputdisplay")
        self.horizontalLayout.addWidget(self.inputdisplay)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ocrbtn = QtWidgets.QPushButton(self.frame_3)
        self.ocrbtn.setMinimumSize(QtCore.QSize(150, 150))
        self.ocrbtn.setMaximumSize(QtCore.QSize(300, 250))
        self.ocrbtn.setStyleSheet("#ocrbtn\n"
"{\n"
"\n"
"border-radius: 20px;\n"
"\n"
"\n"
"}\n"
"\n"
"#ocrbtn:hover\n"
"{\n"
"  \n"
"    background-color: rgba(255, 170, 0,0.2);\n"
"    border: 1px solid orange;\n"
"}")
        self.ocrbtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bgrounds/ocr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ocrbtn.setIcon(icon)
        self.ocrbtn.setIconSize(QtCore.QSize(150, 150))
        self.ocrbtn.setObjectName("ocrbtn")
        self.horizontalLayout_3.addWidget(self.ocrbtn)
        self.htrbtn = QtWidgets.QPushButton(self.frame_3)
        self.htrbtn.setMinimumSize(QtCore.QSize(150, 150))
        self.htrbtn.setMaximumSize(QtCore.QSize(300, 250))
        self.htrbtn.setStyleSheet("#htrbtn\n"
"{\n"
"\n"
"border-radius: 20px;\n"
"\n"
"\n"
"}\n"
"\n"
"#htrbtn:hover\n"
"{\n"
"  \n"
"    background-color: rgba(255, 170, 0,0.2);\n"
"    border: 1px solid orange;\n"
"}")
        self.htrbtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/bgrounds/htr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.htrbtn.setIcon(icon1)
        self.htrbtn.setIconSize(QtCore.QSize(150, 150))
        self.htrbtn.setObjectName("htrbtn")
        self.horizontalLayout_3.addWidget(self.htrbtn)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(100, 60))
        self.label_3.setMaximumSize(QtCore.QSize(700, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("*\n"
"{\n"
"background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"border-radius: 10px;\n"
"    \n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.backbtn = QtWidgets.QPushButton(self.frame_6)
        self.backbtn.setMinimumSize(QtCore.QSize(400, 40))
        self.backbtn.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backbtn.setFont(font)
        self.backbtn.setStyleSheet("*\n"
"{\n"
"\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(170, 0, 0);\n"
"border-radius:10px;\n"
"\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/bgrounds/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backbtn.setIcon(icon2)
        self.backbtn.setIconSize(QtCore.QSize(23, 23))
        self.backbtn.setObjectName("backbtn")
        self.horizontalLayout_5.addWidget(self.backbtn)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        self.backbtn.clicked.connect(self.goback)
        self.htrbtn.clicked.connect(self.htr)
        self.ocrbtn.clicked.connect(self.ocr)

        obj= QtWidgets.QWidget() 
        pixmap = QPixmap("./inputimg/input.png")      
        self.inputdisplay.setPixmap(pixmap)
        obj.resize(pixmap.width(), pixmap.height())

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Recognizer"))
        self.label_3.setText(_translate("MainWindow", "OUTPUT"))
        self.backbtn.setText(_translate("MainWindow", "Back"))

import bg_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

