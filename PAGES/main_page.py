from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem 
from PAGES.main_python import Ui_MainWindow
from PAGES.app_info import AppInfoPage
from PyQt5.QtWidgets import QMessageBox
import os
from PAGES.connections import main as sqlconnection
from PAGES.create_table import main as createTable
import sqlite3 as sql

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionApp_info.triggered.connect(self.open_app_info_page)
        self.info_page=AppInfoPage()
        self.btnListeleClick()
        self.ui.ogr_export_button.hide()
        self.ui.aidat_export_button.hide()
        self.ui.actionExport_Data.toggled[bool].connect(self.btnstate)
        self.ui.register_button.clicked.connect(self.student_add)
        self.ui.ogrenciler_tableWidget.itemSelectionChanged.connect(self.ListOnClick)
        dirName = './db'
        sqlconnection()
        createTable()

        if not os.path.exists(dirName):
            os.makedirs(dirName)
            print("Directory " , dirName ,  " Created ")
        else:    
            print("Directory " , dirName ,  " already exists") 

    def open_app_info_page(self):
        self.info_page.show()

    def btnstate(self,state):
        if (state==True):
            self.ui.ogr_export_button.show()
            self.ui.aidat_export_button.show()
        else:
            self.ui.ogr_export_button.hide()
            self.ui.aidat_export_button.hide()
    def btnListeleClick(self): 
        self.ui.ogrenciler_tableWidget.clear()
        self.ui.ogrenciler_tableWidget.setColumnCount(6)
        self.ui.ogrenciler_tableWidget.setHorizontalHeaderLabels(('TC','Isim/Soyad','Numara','Brans','Kayit','Bitis'))
        self.ui.ogrenciler_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM ogrenciler"
        cur.execute(selectquery) 
        rows = cur.fetchall()
        self.ui.ogrenciler_tableWidget.setRowCount(len(rows))
        
        for satirIndeks, satirVeri in enumerate(rows):
            for sutunIndeks, sutunVeri in enumerate (satirVeri):
                self.ui.ogrenciler_tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri))) 
    def btnTemizle(self):
        self.ui.ogr_tc_edit.clear()
        self.ui.ogr_name_surname_edit.clear()
        self.ui.ogr_number_edit.clear()
        self.ui.register_edit.clear()
        self.ui.register_finish_edit.clear()
    def ListOnClick(self): 
        self.ui.ogr_tc_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 0).text())
        self.ui.ogr_name_surname_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 1).text())
        self.ui.ogr_number_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 2).text())
        self.ui.brans_combox.setCurrentText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 3).text())
        self.ui.register_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 4).text())
        self.ui.register_finish_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 5).text())
    def student_add(self):
        tc=self.ui.ogr_tc_edit.text()
        isim_soyad=self.ui.ogr_name_surname_edit.text()
        numara=self.ui.ogr_number_edit.text()
        brans =self.ui.brans_combox.currentText()
        kayit=self.ui.register_edit.text()
        bitis=self.ui.register_finish_edit.text()

        try:
            self.conn = sql.connect("./db/mxsoftware.db")
            self.c = self.conn.cursor() 
            self.c.execute("INSERT INTO ogrenciler VALUES (?,?,?,?,?,?)",(tc,isim_soyad,numara,brans,kayit,bitis))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            self.ui.statusBar.showMessage("Kayıt Başarılı",5000)
            self.btnTemizle()
        except Exception as error:
            self.ui.statusBar.showMessage("Kayıt Başarısız"+str(error),5000)

    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Close The Window', 'Are you sure you want to close the window?',
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        