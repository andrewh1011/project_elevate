# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addTypeUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(582, 591)
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tutorialBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tutorialBtn.setFont(font)
        self.tutorialBtn.setObjectName("tutorialBtn")
        self.horizontalLayout_3.addWidget(self.tutorialBtn)
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout_3.addWidget(self.saveBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.tNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tNameLabel.setObjectName("tNameLabel")
        self.verticalLayout.addWidget(self.tNameLabel)
        self.colListLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.colListLabel.setFont(font)
        self.colListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.colListLabel.setObjectName("colListLabel")
        self.verticalLayout.addWidget(self.colListLabel)
        self.successCondLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.successCondLabel.setFont(font)
        self.successCondLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.successCondLabel.setObjectName("successCondLabel")
        self.verticalLayout.addWidget(self.successCondLabel)
        self.successInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.successInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.successInfoLabel.setObjectName("successInfoLabel")
        self.verticalLayout.addWidget(self.successInfoLabel)
        self.pendingCondLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pendingCondLabel.setFont(font)
        self.pendingCondLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pendingCondLabel.setObjectName("pendingCondLabel")
        self.verticalLayout.addWidget(self.pendingCondLabel)
        self.pendingInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.pendingInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pendingInfoLabel.setObjectName("pendingInfoLabel")
        self.verticalLayout.addWidget(self.pendingInfoLabel)
        self.failureCondLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.failureCondLabel.setFont(font)
        self.failureCondLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.failureCondLabel.setObjectName("failureCondLabel")
        self.verticalLayout.addWidget(self.failureCondLabel)
        self.failureInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.failureInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.failureInfoLabel.setObjectName("failureInfoLabel")
        self.verticalLayout.addWidget(self.failureInfoLabel)
        self.notAssignedCondLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.notAssignedCondLabel.setFont(font)
        self.notAssignedCondLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.notAssignedCondLabel.setObjectName("notAssignedCondLabel")
        self.verticalLayout.addWidget(self.notAssignedCondLabel)
        self.notAssignedInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.notAssignedInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.notAssignedInfoLabel.setObjectName("notAssignedInfoLabel")
        self.verticalLayout.addWidget(self.notAssignedInfoLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tName = QtWidgets.QLineEdit(self.centralwidget)
        self.tName.setObjectName("tName")
        self.verticalLayout_2.addWidget(self.tName)
        self.colList = QtWidgets.QLineEdit(self.centralwidget)
        self.colList.setMaximumSize(QtCore.QSize(500, 16777215))
        self.colList.setText("")
        self.colList.setObjectName("colList")
        self.verticalLayout_2.addWidget(self.colList)
        self.successCond = QtWidgets.QLineEdit(self.centralwidget)
        self.successCond.setMaximumSize(QtCore.QSize(500, 16777215))
        self.successCond.setText("")
        self.successCond.setObjectName("successCond")
        self.verticalLayout_2.addWidget(self.successCond)
        self.successInfo = QtWidgets.QLineEdit(self.centralwidget)
        self.successInfo.setObjectName("successInfo")
        self.verticalLayout_2.addWidget(self.successInfo)
        self.pendingCond = QtWidgets.QLineEdit(self.centralwidget)
        self.pendingCond.setMaximumSize(QtCore.QSize(500, 16777215))
        self.pendingCond.setText("")
        self.pendingCond.setObjectName("pendingCond")
        self.verticalLayout_2.addWidget(self.pendingCond)
        self.pendingInfo = QtWidgets.QLineEdit(self.centralwidget)
        self.pendingInfo.setObjectName("pendingInfo")
        self.verticalLayout_2.addWidget(self.pendingInfo)
        self.failureCond = QtWidgets.QLineEdit(self.centralwidget)
        self.failureCond.setObjectName("failureCond")
        self.verticalLayout_2.addWidget(self.failureCond)
        self.failureInfo = QtWidgets.QLineEdit(self.centralwidget)
        self.failureInfo.setMaximumSize(QtCore.QSize(500, 16777215))
        self.failureInfo.setText("")
        self.failureInfo.setObjectName("failureInfo")
        self.verticalLayout_2.addWidget(self.failureInfo)
        self.notAssignedCond = QtWidgets.QLineEdit(self.centralwidget)
        self.notAssignedCond.setObjectName("notAssignedCond")
        self.verticalLayout_2.addWidget(self.notAssignedCond)
        self.notAssignedInfo = QtWidgets.QLineEdit(self.centralwidget)
        self.notAssignedInfo.setMaximumSize(QtCore.QSize(500, 16777215))
        self.notAssignedInfo.setText("")
        self.notAssignedInfo.setObjectName("notAssignedInfo")
        self.verticalLayout_2.addWidget(self.notAssignedInfo)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
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
        self.gridLayout.addWidget(self.actionLabel, 4, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 3)
        AddWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 26))
        self.menubar.setObjectName("menubar")
        AddWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddWindow)
        self.statusbar.setObjectName("statusbar")
        AddWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "Add Training Type"))
        self.tutorialBtn.setText(_translate("AddWindow", "Tutorial"))
        self.saveBtn.setText(_translate("AddWindow", "Save"))
        self.tNameLabel.setText(_translate("AddWindow", "Type Name:"))
        self.colListLabel.setText(_translate("AddWindow", "Custom Columns:"))
        self.successCondLabel.setText(_translate("AddWindow", "Success Condition:"))
        self.successInfoLabel.setText(_translate("AddWindow", "Success Info:"))
        self.pendingCondLabel.setText(_translate("AddWindow", "Pending Condition:"))
        self.pendingInfoLabel.setText(_translate("AddWindow", "Pending Info:"))
        self.failureCondLabel.setText(_translate("AddWindow", "Failure Condition:"))
        self.failureInfoLabel.setText(_translate("AddWindow", "Failure Info:"))
        self.notAssignedCondLabel.setText(_translate("AddWindow", "Not Assigned Condition:"))
        self.notAssignedInfoLabel.setText(_translate("AddWindow", "Not Assigned Info:"))
        self.label_5.setText(_translate("AddWindow", "Add a Training Type:"))
