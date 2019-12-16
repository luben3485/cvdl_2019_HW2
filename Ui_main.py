# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\luben\Cvdl_Hw2_20191212\Hw2\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 40, 171, 171))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 240, 171, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 60, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(210, 40, 201, 371))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 100, 131, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 220, 131, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "1. Stereo"))
        self.pushButton.setText(_translate("MainWindow", "1.1 Disparity"))
        self.groupBox_2.setTitle(_translate("MainWindow", "2. Normalized Cross Correlation"))
        self.pushButton_2.setText(_translate("MainWindow", "2.1 NCC"))
        self.groupBox_3.setTitle(_translate("MainWindow", "3. SIFT"))
        self.pushButton_3.setText(_translate("MainWindow", "3.1 Keypoints"))
        self.pushButton_4.setText(_translate("MainWindow", "3.2 Matched keypoints"))
