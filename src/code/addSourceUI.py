# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSourceNewUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(505, 579)
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
        self.gridLayout.addWidget(self.actionLabel, 6, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.typeDdl = QtWidgets.QComboBox(self.centralwidget)
        self.typeDdl.setObjectName("typeDdl")
        self.horizontalLayout.addWidget(self.typeDdl)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sourceNameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.sourceNameLabel.setFont(font)
        self.sourceNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sourceNameLabel.setObjectName("sourceNameLabel")
        self.verticalLayout.addWidget(self.sourceNameLabel)
        self.firstNameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.firstNameLabel.setFont(font)
        self.firstNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.verticalLayout.addWidget(self.firstNameLabel)
        self.lastNameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lastNameLabel.setFont(font)
        self.lastNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.verticalLayout.addWidget(self.lastNameLabel)
        self.dodidLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.dodidLabel.setFont(font)
        self.dodidLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dodidLabel.setObjectName("dodidLabel")
        self.verticalLayout.addWidget(self.dodidLabel)
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.emailLabel.setFont(font)
        self.emailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.emailLabel.setObjectName("emailLabel")
        self.verticalLayout.addWidget(self.emailLabel)
        self.courseNameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.courseNameLabel.setFont(font)
        self.courseNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.verticalLayout.addWidget(self.courseNameLabel)
        self.skipRowsLabel = QtWidgets.QLabel(self.centralwidget)
        self.skipRowsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.skipRowsLabel.setObjectName("skipRowsLabel")
        self.verticalLayout.addWidget(self.skipRowsLabel)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)
        self.dynamicLabelVL = QtWidgets.QVBoxLayout()
        self.dynamicLabelVL.setObjectName("dynamicLabelVL")
        self.gridLayout.addLayout(self.dynamicLabelVL, 3, 0, 1, 1)
        self.dynamicIndexVL = QtWidgets.QVBoxLayout()
        self.dynamicIndexVL.setObjectName("dynamicIndexVL")
        self.gridLayout.addLayout(self.dynamicIndexVL, 3, 1, 1, 1)
        AddWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 26))
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
        self.label.setText(_translate("AddWindow", "Type:"))
        self.sourceNameLabel.setText(_translate("AddWindow", "Source Name:"))
        self.firstNameLabel.setText(_translate("AddWindow", "First Name:"))
        self.lastNameLabel.setText(_translate("AddWindow", "Last Name:"))
        self.dodidLabel.setText(_translate("AddWindow", "DODID:"))
        self.emailLabel.setText(_translate("AddWindow", "Email:"))
        self.courseNameLabel.setText(_translate("AddWindow", "Course Name:"))
        self.skipRowsLabel.setText(_translate("AddWindow", "Header Rows:"))
        self.tutorialBtn.setText(_translate("AddWindow", "Tutorial"))
        self.saveSourceBtn.setText(_translate("AddWindow", "Save"))
