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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.ay_cmb_aidat = QtWidgets.QComboBox(Form)
        self.ay_cmb_aidat.setObjectName("ay_cmb_aidat")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.ay_cmb_aidat.addItem("")
        self.horizontalLayout_4.addWidget(self.ay_cmb_aidat)
        self.yil_cmb_aidat = QtWidgets.QComboBox(Form)
        self.yil_cmb_aidat.setObjectName("yil_cmb_aidat")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.yil_cmb_aidat.addItem("")
        self.horizontalLayout_4.addWidget(self.yil_cmb_aidat)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
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
        self.add_aidat_button = QtWidgets.QPushButton(Form)
        self.add_aidat_button.setObjectName("add_aidat_button")
        self.horizontalLayout_2.addWidget(self.add_aidat_button)
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_2.addWidget(self.exit_button)
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
        self.label_2.setText(_translate("Form", "Tarih    :"))
        self.ay_cmb_aidat.setItemText(0, _translate("Form", "OCAK"))
        self.ay_cmb_aidat.setItemText(1, _translate("Form", "ŞUBAT"))
        self.ay_cmb_aidat.setItemText(2, _translate("Form", "MART"))
        self.ay_cmb_aidat.setItemText(3, _translate("Form", "NİSAN"))
        self.ay_cmb_aidat.setItemText(4, _translate("Form", "MAYIS"))
        self.ay_cmb_aidat.setItemText(5, _translate("Form", "HAZİRAN"))
        self.ay_cmb_aidat.setItemText(6, _translate("Form", "TEMMUZ"))
        self.ay_cmb_aidat.setItemText(7, _translate("Form", "AĞUSTOS"))
        self.ay_cmb_aidat.setItemText(8, _translate("Form", "EYLÜL"))
        self.ay_cmb_aidat.setItemText(9, _translate("Form", "EKİM"))
        self.ay_cmb_aidat.setItemText(10, _translate("Form", "KASIM"))
        self.ay_cmb_aidat.setItemText(11, _translate("Form", "ARALIK"))
        self.yil_cmb_aidat.setItemText(0, _translate("Form", "2022"))
        self.yil_cmb_aidat.setItemText(1, _translate("Form", "2023"))
        self.yil_cmb_aidat.setItemText(2, _translate("Form", "2024"))
        self.yil_cmb_aidat.setItemText(3, _translate("Form", "2025"))
        self.yil_cmb_aidat.setItemText(4, _translate("Form", "2026"))
        self.yil_cmb_aidat.setItemText(5, _translate("Form", "2027"))
        self.yil_cmb_aidat.setItemText(6, _translate("Form", "2028"))
        self.yil_cmb_aidat.setItemText(7, _translate("Form", "2029"))
        self.yil_cmb_aidat.setItemText(8, _translate("Form", "2030"))
        self.yil_cmb_aidat.setItemText(9, _translate("Form", "2031"))
        self.yil_cmb_aidat.setItemText(10, _translate("Form", "2032"))
        self.yil_cmb_aidat.setItemText(11, _translate("Form", "2033"))
        self.yil_cmb_aidat.setItemText(12, _translate("Form", "2034"))
        self.yil_cmb_aidat.setItemText(13, _translate("Form", "2035"))
        self.yil_cmb_aidat.setItemText(14, _translate("Form", "2036"))
        self.yil_cmb_aidat.setItemText(15, _translate("Form", "2037"))
        self.yil_cmb_aidat.setItemText(16, _translate("Form", "2038"))
        self.yil_cmb_aidat.setItemText(17, _translate("Form", "2039"))
        self.yil_cmb_aidat.setItemText(18, _translate("Form", "2040"))
        self.label_3.setText(_translate("Form", "Ücret:    "))
        self.money_lineEdit.setInputMask(_translate("Form", "99999"))
        self.add_aidat_button.setText(_translate("Form", "Ekle"))
        self.exit_button.setText(_translate("Form", "Exit"))

import assets.py_rc.icons_rc as icons_rc
