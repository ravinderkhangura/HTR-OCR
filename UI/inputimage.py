# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputimage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from takephoto import Ui_takephotowindow
from uploadimage import Ui_uploadimgwindow

class Ui_inputimage(object):
    

    def opentakephoto(self):
        try:
            self.window=QtWidgets.QMainWindow()
            self.ui2= Ui_takephotowindow()
            self.ui2.setupUi(self.window)
            inputimage = QtWidgets.QMainWindow()
            ui = Ui_inputimage()
            ui.setupUi(inputimage)
            inputimage.close()
            self.window.show()

        except Exception as ex:
            print(ex)
        

    def openuploadimage(self):
        try:
            self.window=QtWidgets.QMainWindow()
            self.ui2= Ui_uploadimgwindow()
            self.ui2.setupUi(self.window)
            inputimage = QtWidgets.QMainWindow()
            ui = Ui_inputimage()
            ui.setupUi(inputimage)
            inputimage.close()
            self.window.show()
            #inputimage.hide()
            #inputimage.exec_()
        except Exception as ex:
            print(ex)

        
        

        
    def setupUi(self, inputimage):
        inputimage.setObjectName("inputimage")
        inputimage.resize(601, 425)
        inputimage.setStyleSheet("*{\n"
"\n"
"background-color:white;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(inputimage)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.heading = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setFocusPolicy(QtCore.Qt.NoFocus)
        self.heading.setStyleSheet("#heading{\n"
"\n"
"color: orange;\n"
"shadow-text: 3px 3xp 3px black;\n"
"\n"
"         \n"
"}\n"
"\n"
"*{\n"
" background:#d6d6d6;\n"
"border-radius: 20px;\n"
"\n"
"}")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.verticalLayout_2.addWidget(self.heading)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.takephotobtn = QtWidgets.QPushButton(self.frame_5)
        self.takephotobtn.setMinimumSize(QtCore.QSize(0, 165))
        self.takephotobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.takephotobtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.takephotobtn.setStyleSheet("QPushButton{\n"
"\n"
"border-radius:25px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"border:1px solid orange;\n"
" box-shadow:3px 3px 6px black;\n"
"background: rgba(255, 191, 0,0.1)\n"
"\n"
"}")
        self.takephotobtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bgrounds/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.takephotobtn.setIcon(icon)
        self.takephotobtn.setIconSize(QtCore.QSize(155, 155))
        self.takephotobtn.setDefault(False)
        self.takephotobtn.setFlat(True)
        self.takephotobtn.setObjectName("takephotobtn")
        self.verticalLayout_3.addWidget(self.takephotobtn)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uploadphotobtn = QtWidgets.QPushButton(self.frame_6)
        self.uploadphotobtn.setMinimumSize(QtCore.QSize(0, 165))
        self.uploadphotobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uploadphotobtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.uploadphotobtn.setStyleSheet("QPushButton{\n"
"\n"
"border-radius:25px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"border:1px solid orange;\n"
" box-shadow:3px 3px 6px black;\n"
"background: rgba(255, 191, 0,0.1);\n"
"\n"
"}")
        self.uploadphotobtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/bgrounds/uploadicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadphotobtn.setIcon(icon1)
        self.uploadphotobtn.setIconSize(QtCore.QSize(147, 147))
        self.uploadphotobtn.setFlat(True)
        self.uploadphotobtn.setObjectName("uploadphotobtn")
        self.verticalLayout_4.addWidget(self.uploadphotobtn)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        inputimage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(inputimage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 18))
        self.menubar.setObjectName("menubar")
        inputimage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(inputimage)
        self.statusbar.setObjectName("statusbar")
        inputimage.setStatusBar(self.statusbar)

        self.retranslateUi(inputimage)
        QtCore.QMetaObject.connectSlotsByName(inputimage)

        self.takephotobtn.clicked.connect(self.opentakephoto)
        self.uploadphotobtn.clicked.connect(self.openuploadimage)

    def retranslateUi(self, inputimage):
        _translate = QtCore.QCoreApplication.translate
        inputimage.setWindowTitle(_translate("inputimage", "MainWindow"))
        self.heading.setText(_translate("inputimage", "PICTURE"))
        self.label_2.setText(_translate("inputimage", "Take Photo"))
        self.label_3.setText(_translate("inputimage", "Upload Photo"))

import bg_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inputimage = QtWidgets.QMainWindow()
    ui = Ui_inputimage()
    ui.setupUi(inputimage)
    inputimage.show()
    sys.exit(app.exec_())

