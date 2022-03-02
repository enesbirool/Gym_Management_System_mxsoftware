# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/project/assets/GUI/main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1100, 539)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setSizeIncrement(QtCore.QSize(800, 200))
        MainWindow.setBaseSize(QtCore.QSize(700, 200))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/martialarts_g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1100, 400))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ogr_tc_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ogr_tc_edit.setObjectName("ogr_tc_edit")
        self.horizontalLayout.addWidget(self.ogr_tc_edit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.ogr_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ogr_name_edit.setPlaceholderText("")
        self.ogr_name_edit.setObjectName("ogr_name_edit")
        self.horizontalLayout_5.addWidget(self.ogr_name_edit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.ogr_surname_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ogr_surname_lineEdit.setObjectName("ogr_surname_lineEdit")
        self.horizontalLayout_10.addWidget(self.ogr_surname_lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ogr_number_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ogr_number_edit.setInputMask("")
        self.ogr_number_edit.setObjectName("ogr_number_edit")
        self.horizontalLayout_2.addWidget(self.ogr_number_edit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.brans_combox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brans_combox.sizePolicy().hasHeightForWidth())
        self.brans_combox.setSizePolicy(sizePolicy)
        self.brans_combox.setMinimumSize(QtCore.QSize(10, 10))
        self.brans_combox.setObjectName("brans_combox")
        self.brans_combox.addItem("")
        self.brans_combox.addItem("")
        self.brans_combox.addItem("")
        self.brans_combox.addItem("")
        self.brans_combox.addItem("")
        self.horizontalLayout_3.addWidget(self.brans_combox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.register_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.register_dateEdit.setCalendarPopup(True)
        self.register_dateEdit.setObjectName("register_dateEdit")
        self.horizontalLayout_7.addWidget(self.register_dateEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.register_finish_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.register_finish_dateEdit.setCalendarPopup(True)
        self.register_finish_dateEdit.setObjectName("register_finish_dateEdit")
        self.horizontalLayout_4.addWidget(self.register_finish_dateEdit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.ogrenciler_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.ogrenciler_tableWidget.setMinimumSize(QtCore.QSize(600, 200))
        self.ogrenciler_tableWidget.setSizeIncrement(QtCore.QSize(600, 200))
        self.ogrenciler_tableWidget.setBaseSize(QtCore.QSize(600, 200))
        self.ogrenciler_tableWidget.setStatusTip("")
        self.ogrenciler_tableWidget.setAutoFillBackground(True)
        self.ogrenciler_tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ogrenciler_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ogrenciler_tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ogrenciler_tableWidget.setLineWidth(1)
        self.ogrenciler_tableWidget.setAutoScrollMargin(16)
        self.ogrenciler_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ogrenciler_tableWidget.setRowCount(100)
        self.ogrenciler_tableWidget.setObjectName("ogrenciler_tableWidget")
        self.ogrenciler_tableWidget.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.ogrenciler_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ogrenciler_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ogrenciler_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ogrenciler_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ogrenciler_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ogrenciler_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ogrenciler_tableWidget.setHorizontalHeaderItem(6, item)
        self.ogrenciler_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.ogrenciler_tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.ogrenciler_tableWidget.horizontalHeader().setHighlightSections(True)
        self.ogrenciler_tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.ogrenciler_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.ogrenciler_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ogrenciler_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.ogrenciler_tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.horizontalLayout_6.addWidget(self.ogrenciler_tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setObjectName("register_button")
        self.verticalLayout_6.addWidget(self.register_button)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout_6.addWidget(self.delete_button)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setObjectName("update_button")
        self.verticalLayout_7.addWidget(self.update_button)
        self.more_detail_button = QtWidgets.QPushButton(self.centralwidget)
        self.more_detail_button.setObjectName("more_detail_button")
        self.verticalLayout_7.addWidget(self.more_detail_button)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setObjectName("search_button")
        self.verticalLayout_8.addWidget(self.search_button)
        self.serach_all_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.serach_all_pushButton.setObjectName("serach_all_pushButton")
        self.verticalLayout_8.addWidget(self.serach_all_pushButton)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.aidat_add_button = QtWidgets.QPushButton(self.centralwidget)
        self.aidat_add_button.setObjectName("aidat_add_button")
        self.verticalLayout_3.addWidget(self.aidat_add_button)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.aidat_export_button = QtWidgets.QPushButton(self.centralwidget)
        self.aidat_export_button.setObjectName("aidat_export_button")
        self.horizontalLayout_9.addWidget(self.aidat_export_button)
        self.ogr_export_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ogr_export_button.sizePolicy().hasHeightForWidth())
        self.ogr_export_button.setSizePolicy(sizePolicy)
        self.ogr_export_button.setObjectName("ogr_export_button")
        self.horizontalLayout_9.addWidget(self.ogr_export_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(200, 100))
        self.label_8.setStyleSheet("image: url(:/assets/martialarts_g.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.aidatlar_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.aidatlar_tableWidget.setMinimumSize(QtCore.QSize(600, 200))
        self.aidatlar_tableWidget.setSizeIncrement(QtCore.QSize(600, 200))
        self.aidatlar_tableWidget.setBaseSize(QtCore.QSize(600, 200))
        self.aidatlar_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aidatlar_tableWidget.setAutoScrollMargin(16)
        self.aidatlar_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.aidatlar_tableWidget.setDragEnabled(False)
        self.aidatlar_tableWidget.setShowGrid(True)
        self.aidatlar_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.aidatlar_tableWidget.setWordWrap(True)
        self.aidatlar_tableWidget.setCornerButtonEnabled(True)
        self.aidatlar_tableWidget.setRowCount(100)
        self.aidatlar_tableWidget.setObjectName("aidatlar_tableWidget")
        self.aidatlar_tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.aidatlar_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.aidatlar_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.aidatlar_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.aidatlar_tableWidget.setHorizontalHeaderItem(3, item)
        self.aidatlar_tableWidget.horizontalHeader().setVisible(True)
        self.aidatlar_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.aidatlar_tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.aidatlar_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.aidatlar_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.aidatlar_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.aidatlar_tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.aidatlar_tableWidget.verticalHeader().setHighlightSections(True)
        self.aidatlar_tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.aidatlar_tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.aidatlar_tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_8.addWidget(self.aidatlar_tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuSettings = QtWidgets.QMenu(self.menuMenu)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExport_Data = QtWidgets.QAction(MainWindow)
        self.actionExport_Data.setCheckable(True)
        self.actionExport_Data.setObjectName("actionExport_Data")
        self.actionlicence_sozlesme = QtWidgets.QAction(MainWindow)
        self.actionlicence_sozlesme.setObjectName("actionlicence_sozlesme")
        self.export_to_database_action = QtWidgets.QAction(MainWindow)
        self.export_to_database_action.setObjectName("export_to_database_action")
        self.actionBilgi_Boloncuklar = QtWidgets.QAction(MainWindow)
        self.actionBilgi_Boloncuklar.setCheckable(True)
        self.actionBilgi_Boloncuklar.setObjectName("actionBilgi_Boloncuklar")
        self.actionLoad_Database = QtWidgets.QAction(MainWindow)
        self.actionLoad_Database.setObjectName("actionLoad_Database")
        self.actionSave_Database = QtWidgets.QAction(MainWindow)
        self.actionSave_Database.setObjectName("actionSave_Database")
        self.actionLoad_Database_2 = QtWidgets.QAction(MainWindow)
        self.actionLoad_Database_2.setObjectName("actionLoad_Database_2")
        self.actionBilgi_Boloncuklar_2 = QtWidgets.QAction(MainWindow)
        self.actionBilgi_Boloncuklar_2.setCheckable(True)
        self.actionBilgi_Boloncuklar_2.setObjectName("actionBilgi_Boloncuklar_2")
        self.actionApp_nfo = QtWidgets.QAction(MainWindow)
        self.actionApp_nfo.setObjectName("actionApp_nfo")
        self.actionToplu_Mail_G_nder = QtWidgets.QAction(MainWindow)
        self.actionToplu_Mail_G_nder.setObjectName("actionToplu_Mail_G_nder")
        self.menuSettings.addAction(self.actionToplu_Mail_G_nder)
        self.menuSettings.addAction(self.actionBilgi_Boloncuklar_2)
        self.menuSettings.addAction(self.actionSave_Database)
        self.menuSettings.addAction(self.actionLoad_Database_2)
        self.menuMenu.addAction(self.actionExport_Data)
        self.menuMenu.addAction(self.menuSettings.menuAction())
        self.menuMenu.addAction(self.actionlicence_sozlesme)
        self.menuMenu.addAction(self.actionApp_nfo)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sporcu Kayıt ve Aidat Programı"))
        self.label.setText(_translate("MainWindow", "Öğrenci TC    :   "))
        self.ogr_tc_edit.setInputMask(_translate("MainWindow", "99999999999"))
        self.ogr_tc_edit.setPlaceholderText(_translate("MainWindow", "11 rakam uzunluğunda olmalı"))
        self.label_5.setText(_translate("MainWindow", "İsim               :   "))
        self.label_10.setText(_translate("MainWindow", "Soyad           :    "))
        self.label_2.setText(_translate("MainWindow", "Telefon         :    "))
        self.ogr_number_edit.setPlaceholderText(_translate("MainWindow", "+90 (---) --- -- --"))
        self.label_3.setText(_translate("MainWindow", "Branş            :    "))
        self.brans_combox.setItemText(0, _translate("MainWindow", "Taekwondo"))
        self.brans_combox.setItemText(1, _translate("MainWindow", "Judo"))
        self.brans_combox.setItemText(2, _translate("MainWindow", "Pilates"))
        self.brans_combox.setItemText(3, _translate("MainWindow", "Karate"))
        self.brans_combox.setItemText(4, _translate("MainWindow", "Fitness"))
        self.label_4.setText(_translate("MainWindow", "Kayıt Tarihi    :    "))
        self.register_dateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.label_6.setText(_translate("MainWindow", "Kayıt Bitiş       :   "))
        self.register_finish_dateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        item = self.ogrenciler_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TC"))
        item = self.ogrenciler_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "İsim"))
        item = self.ogrenciler_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Soyad"))
        item = self.ogrenciler_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefon"))
        item = self.ogrenciler_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Branş"))
        item = self.ogrenciler_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Kayıt"))
        item = self.ogrenciler_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Bitiş"))
        self.register_button.setText(_translate("MainWindow", "Kayıt"))
        self.delete_button.setText(_translate("MainWindow", "Sil"))
        self.update_button.setText(_translate("MainWindow", "Güncelle"))
        self.more_detail_button.setText(_translate("MainWindow", "Detaylar"))
        self.search_button.setText(_translate("MainWindow", "Öğrenci Ara"))
        self.serach_all_pushButton.setText(_translate("MainWindow", "Tüm Sonuçlar"))
        self.aidat_add_button.setText(_translate("MainWindow", "Aidat Ekle"))
        self.aidat_export_button.setText(_translate("MainWindow", "Aidatlar Export to Excel"))
        self.ogr_export_button.setText(_translate("MainWindow", "Öğrenciler Export to Excel"))
        self.aidatlar_tableWidget.setSortingEnabled(False)
        item = self.aidatlar_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TC"))
        item = self.aidatlar_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "İsim"))
        item = self.aidatlar_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tarih"))
        item = self.aidatlar_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ücret"))
        self.label_9.setText(_translate("MainWindow", "Copyright © MXSoftware 2022 Tüm Hakları Saklıdır. Coded By Enes Birol"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuSettings.setTitle(_translate("MainWindow", "Ayarlar"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExport_Data.setText(_translate("MainWindow", "Excel Çıktısı Al"))
        self.actionlicence_sozlesme.setText(_translate("MainWindow", "Lisans Sözleşmesi"))
        self.export_to_database_action.setText(_translate("MainWindow", "Save Database"))
        self.actionBilgi_Boloncuklar.setText(_translate("MainWindow", "Bilgi Boloncukları"))
        self.actionLoad_Database.setText(_translate("MainWindow", "Load Database"))
        self.actionSave_Database.setText(_translate("MainWindow", "Save Database"))
        self.actionLoad_Database_2.setText(_translate("MainWindow", "Load Database"))
        self.actionBilgi_Boloncuklar_2.setText(_translate("MainWindow", "Bilgi Boloncukları"))
        self.actionApp_nfo.setText(_translate("MainWindow", "Uygulama Hakkında"))
        self.actionToplu_Mail_G_nder.setText(_translate("MainWindow", "Toplu Mail Gönder"))
        self.register_dateEdit.setDate(datetime.date.today())
        self.register_finish_dateEdit.setDate(datetime.date.today())

import assets.py_rc.icons_rc as icons_rc
