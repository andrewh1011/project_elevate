# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(928, 494)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Dialog.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.saveSourceBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveSourceBtn.setGeometry(QtCore.QRect(170, 390, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.saveSourceBtn.setFont(font)
        self.saveSourceBtn.setObjectName("saveSourceBtn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.actionLabel = QtWidgets.QLabel(self.centralwidget)
        self.actionLabel.setGeometry(QtCore.QRect(360, 410, 521, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.actionLabel.setFont(font)
        self.actionLabel.setMouseTracking(False)
        self.actionLabel.setText("")
        self.actionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actionLabel.setObjectName("actionLabel")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(540, 320, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.startBtn.setFont(font)
        self.startBtn.setStyleSheet("background-color: #33b249;\n"
"border: none;\n"
"color: #FFFFFF;\n"
"border-radius: 4px;\n"
"box-shadow: rgba(0, 0, 0, 0.1) 0 2px 4px;\n"
"padding: 20px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"margin: 4px 2px;")
        self.startBtn.setObjectName("startBtn")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 70, 100, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 70, 161, 311))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sourceName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.sourceName.setText("")
        self.sourceName.setObjectName("sourceName")
        self.verticalLayout_2.addWidget(self.sourceName)
        self.firstName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.firstName.setText("")
        self.firstName.setObjectName("firstName")
        self.verticalLayout_2.addWidget(self.firstName)
        self.lastName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lastName.setText("")
        self.lastName.setObjectName("lastName")
        self.verticalLayout_2.addWidget(self.lastName)
        self.dueDate = QtWidgets.QLineEdit(self.layoutWidget1)
        self.dueDate.setText("")
        self.dueDate.setObjectName("dueDate")
        self.verticalLayout_2.addWidget(self.dueDate)
        self.compDate = QtWidgets.QLineEdit(self.layoutWidget1)
        self.compDate.setText("")
        self.compDate.setObjectName("compDate")
        self.verticalLayout_2.addWidget(self.compDate)
        self.dodid = QtWidgets.QLineEdit(self.layoutWidget1)
        self.dodid.setText("")
        self.dodid.setObjectName("dodid")
        self.verticalLayout_2.addWidget(self.dodid)
        self.email = QtWidgets.QLineEdit(self.layoutWidget1)
        self.email.setText("")
        self.email.setObjectName("email")
        self.verticalLayout_2.addWidget(self.email)
        self.courseName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.courseName.setText("")
        self.courseName.setObjectName("courseName")
        self.verticalLayout_2.addWidget(self.courseName)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(350, 20, 538, 275))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.sourceList = QtWidgets.QListWidget(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.sourceList.setFont(font)
        self.sourceList.setObjectName("sourceList")
        self.verticalLayout_3.addWidget(self.sourceList)
        self.deleteSourceBtn = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.deleteSourceBtn.setFont(font)
        self.deleteSourceBtn.setObjectName("deleteSourceBtn")
        self.verticalLayout_3.addWidget(self.deleteSourceBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.fileList = QtWidgets.QListWidget(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.fileList.setFont(font)
        self.fileList.setObjectName("fileList")
        self.verticalLayout_4.addWidget(self.fileList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteFileBtn = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.deleteFileBtn.setFont(font)
        self.deleteFileBtn.setObjectName("deleteFileBtn")
        self.horizontalLayout.addWidget(self.deleteFileBtn)
        self.importButton = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.importButton.setFont(font)
        self.importButton.setObjectName("importButton")
        self.horizontalLayout.addWidget(self.importButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        Dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 37))
        self.menubar.setObjectName("menubar")
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Project Elevate"))
        self.saveSourceBtn.setText(_translate("Dialog", "Save"))
        self.label_5.setText(_translate("Dialog", "Add a data source:"))
        self.startBtn.setText(_translate("Dialog", "Create output"))
        self.label_2.setText(_translate("Dialog", "Source Name:"))
        self.label_6.setText(_translate("Dialog", "First Name:"))
        self.label_9.setText(_translate("Dialog", "Last Name:"))
        self.label_3.setText(_translate("Dialog", "Date Due:"))
        self.label_10.setText(_translate("Dialog", "Date Completed:"))
        self.label_4.setText(_translate("Dialog", "DODID:"))
        self.label_11.setText(_translate("Dialog", "Email:"))
        self.label_12.setText(_translate("Dialog", "Course Name:"))
        self.label_7.setText(_translate("Dialog", "Sources"))
        self.deleteSourceBtn.setText(_translate("Dialog", "Delete Source"))
        self.label_8.setText(_translate("Dialog", "Files"))
        self.deleteFileBtn.setText(_translate("Dialog", "Delete File"))
        self.importButton.setText(_translate("Dialog", "Import"))
