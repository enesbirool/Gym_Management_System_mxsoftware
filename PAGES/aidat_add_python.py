# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/project/PAGES/GUI/aidat_add.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 150)
        Form.setMinimumSize(QtCore.QSize(300, 100))
        Form.setMaximumSize(QtCore.QSize(300, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/martialarts_g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.aidat_comboBox = QtWidgets.QComboBox(Form)
        self.aidat_comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.aidat_comboBox.setObjectName("aidat_comboBox")
        self.horizontalLayout.addWidget(self.aidat_comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.money_lineEdit = QtWidgets.QLineEdit(Form)
        self.money_lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.money_lineEdit.setObjectName("money_lineEdit")
        self.horizontalLayout_3.addWidget(self.money_lineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.add_pushButton_2 = QtWidgets.QPushButton(Form)
        self.add_pushButton_2.setObjectName("add_pushButton_2")
        self.horizontalLayout_2.addWidget(self.add_pushButton_2)
        self.exit_pushButton = QtWidgets.QPushButton(Form)
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.horizontalLayout_2.addWidget(self.exit_pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("background: transparent;\n"
"image: url(:/assets/info.png);")
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aidat Ekle"))
        self.label.setText(_translate("Form", "Öğrenci Adı:"))
        self.label_3.setText(_translate("Form", "Ücret:    "))
        self.money_lineEdit.setInputMask(_translate("Form", "99999"))
        self.add_pushButton_2.setText(_translate("Form", "Ekle"))
        self.exit_pushButton.setText(_translate("Form", "Exit"))

import icons_rc
