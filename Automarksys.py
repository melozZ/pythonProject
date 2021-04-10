# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Automarksys.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(703, 357)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 250, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 250, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 250, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(60, 20, 211, 191))
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(Frame)
        self.listView.setGeometry(QtCore.QRect(310, 30, 256, 192))
        self.listView.setObjectName("listView")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton.setText(_translate("Frame", "答案摄像头OCR"))
        self.pushButton_2.setText(_translate("Frame", "答案判分"))
        self.pushButton_3.setText(_translate("Frame", "答案图片OCR"))
        self.label.setText(_translate("Frame", "            图片未导入"))
