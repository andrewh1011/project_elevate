# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSourceUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(413, 579)
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sourceName = QtWidgets.QLineEdit(self.centralwidget)
        self.sourceName.setMaximumSize(QtCore.QSize(500, 16777215))
        self.sourceName.setText("")
        self.sourceName.setObjectName("sourceName")
        self.verticalLayout_2.addWidget(self.sourceName)
        self.firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName.setMaximumSize(QtCore.QSize(500, 16777215))
        self.firstName.setText("")
        self.firstName.setObjectName("firstName")
        self.verticalLayout_2.addWidget(self.firstName)
        self.lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lastName.setText("")
        self.lastName.setObjectName("lastName")
        self.verticalLayout_2.addWidget(self.lastName)
        self.dueDate = QtWidgets.QLineEdit(self.centralwidget)
        self.dueDate.setMaximumSize(QtCore.QSize(500, 16777215))
        self.dueDate.setText("")
        self.dueDate.setObjectName("dueDate")
        self.verticalLayout_2.addWidget(self.dueDate)
        self.compDate = QtWidgets.QLineEdit(self.centralwidget)
        self.compDate.setMaximumSize(QtCore.QSize(500, 16777215))
        self.compDate.setText("")
        self.compDate.setObjectName("compDate")
        self.verticalLayout_2.addWidget(self.compDate)
        self.dodid = QtWidgets.QLineEdit(self.centralwidget)
        self.dodid.setMaximumSize(QtCore.QSize(500, 16777215))
        self.dodid.setText("")
        self.dodid.setObjectName("dodid")
        self.verticalLayout_2.addWidget(self.dodid)
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setMaximumSize(QtCore.QSize(500, 16777215))
        self.email.setText("")
        self.email.setObjectName("email")
        self.verticalLayout_2.addWidget(self.email)
        self.courseName = QtWidgets.QLineEdit(self.centralwidget)
        self.courseName.setMaximumSize(QtCore.QSize(500, 16777215))
        self.courseName.setText("")
        self.courseName.setObjectName("courseName")
        self.verticalLayout_2.addWidget(self.courseName)
        self.skipRows = QtWidgets.QLineEdit(self.centralwidget)
        self.skipRows.setObjectName("skipRows")
        self.verticalLayout_2.addWidget(self.skipRows)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tutorialBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tutorialBtn.setFont(font)
        self.tutorialBtn.setObjectName("tutorialBtn")
        self.horizontalLayout_3.addWidget(self.tutorialBtn)
        self.saveSourceBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.saveSourceBtn.setFont(font)
        self.saveSourceBtn.setObjectName("saveSourceBtn")
        self.horizontalLayout_3.addWidget(self.saveSourceBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.actionLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionLabel.sizePolicy().hasHeightForWidth())
        self.actionLabel.setSizePolicy(sizePolicy)
        self.actionLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.actionLabel.setText("")
        self.actionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actionLabel.setObjectName("actionLabel")
        self.gridLayout.addWidget(self.actionLabel, 3, 0, 1, 2)
        AddWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 413, 26))
        self.menubar.setObjectName("menubar")
        AddWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddWindow)
        self.statusbar.setObjectName("statusbar")
        AddWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "Add Source"))
        self.label_5.setText(_translate("AddWindow", "Add a data source:"))
        self.label_2.setText(_translate("AddWindow", "Source Name:"))
        self.label_6.setText(_translate("AddWindow", "First Name:"))
        self.label_9.setText(_translate("AddWindow", "Last Name:"))
        self.label_3.setText(_translate("AddWindow", "Date Due:"))
        self.label_10.setText(_translate("AddWindow", "Date Completed:"))
        self.label_4.setText(_translate("AddWindow", "DODID:"))
        self.label_11.setText(_translate("AddWindow", "Email:"))
        self.label_12.setText(_translate("AddWindow", "Course Name:"))
        self.label.setText(_translate("AddWindow", "Header Rows:"))
        self.tutorialBtn.setText(_translate("AddWindow", "Tutorial"))
        self.saveSourceBtn.setText(_translate("AddWindow", "Save"))
