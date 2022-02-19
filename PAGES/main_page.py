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
import pandas as pd
class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        sqlconnection()
        createTable()

        self.btnListeleClick()
        self.info_page=AppInfoPage()

        self.ui.actionApp_info.triggered.connect(self.open_app_info_page)                    
        self.ui.ogr_export_button.hide()
        self.ui.aidat_export_button.hide()
        self.ui.actionExport_Data.toggled[bool].connect(self.btnstate)
        self.ui.register_button.clicked.connect(self.student_add)
        self.ui.delete_button.clicked.connect(self.btnSilClick)
        self.ui.ogrenciler_tableWidget.itemSelectionChanged.connect(self.ListOnClick)
        self.ui.ogr_export_button.clicked.connect(self.exportToExcelOgr) 
        self.ui.aidat_export_button.clicked.connect(self.exportToExcelAidat)

##################### SUPPORTS #############################################       

    def btnstate(self,state):
        if (state==True):
            self.ui.ogr_export_button.show()
            self.ui.aidat_export_button.show()
            self.ui.statusBar.showMessage("Export Butonları Aktif...",5000)
        else:
            self.ui.ogr_export_button.hide()
            self.ui.aidat_export_button.hide()
            self.ui.statusBar.showMessage("Export Butonları Gizlendi...",5000)

    def btnTemizle(self):
        self.ui.ogr_tc_edit.clear()
        self.ui.ogr_name_surname_edit.clear()
        self.ui.ogr_number_edit.clear()
        self.ui.register_edit.clear()
        self.ui.register_finish_edit.clear()

    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Close The Window', 'Are you sure you want to close the window?',
			QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            self.ui.statusBar.showMessage("Çıkış İptal Edildi...",5000)
    def open_app_info_page(self):
        self.info_page.show()


################################# CRUD OPERATIONS #############################

    def btnListeleClick(self): 
        self.ui.ogrenciler_tableWidget.clear()
        self.ui.ogrenciler_tableWidget.setColumnCount(6)
        self.ui.ogrenciler_tableWidget.setHorizontalHeaderLabels(('TC','Ad/Soyad','Numara','Brans','Kayit','Bitis'))
        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM ogrenciler"
        cur.execute(selectquery) 
        rows = cur.fetchall()
        self.ui.ogrenciler_tableWidget.setRowCount(len(rows))
        
        for satirIndeks, satirVeri in enumerate(rows):
            for sutunIndeks, sutunVeri in enumerate (satirVeri):
                self.ui.ogrenciler_tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri))) 

    def ListOnClick(self): 
        self.ui.ogr_tc_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 0).text())
        self.ui.ogr_name_surname_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 1).text())
        self.ui.ogr_number_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 2).text())
        self.ui.brans_combox.setCurrentText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 3).text())
        self.ui.register_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 4).text())
        self.ui.register_finish_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 5).text())
        
    def btnSilClick(self): 
        id = self.ui.ogr_tc_edit.text()
        name= self.ui.ogr_name_surname_edit.text() 
        if  len(id)!=0:
            reply = QMessageBox.question(self, 'Delete Window', 'Are you sure you want to delete this student? '+name,
			QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    self.conn = sql.connect("./db/mxsoftware.db")
                    self.c = self.conn.cursor() 
                    self.c.execute('DELETE FROM ogrenciler WHERE tc = ?  ', (id,))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.ui.statusBar.showMessage(name+" Başarıyla Silindi...",6000)              
                except Exception:
                    print('Error', 'Could not delete student to the database.')
                self.btnListeleClick()
                self.btnTemizle()
            else:
                self.ui.statusBar.showMessage("Silmekten Vazgeçildi...",5000)
        else:            
            self.ui.statusBar.showMessage("Silmek İçin Lütfen Bir Öğrenci Seçin...",5000)
    def student_add(self):
        tc=self.ui.ogr_tc_edit.text()
        isim_soyad=self.ui.ogr_name_surname_edit.text()
        numara=self.ui.ogr_number_edit.text()
        brans =self.ui.brans_combox.currentText()
        kayit=self.ui.register_edit.text()
        bitis=self.ui.register_finish_edit.text()
        if(len(tc)!=0 and len(isim_soyad)!=0 and len(numara)!=0 and len(bitis)!=0):
            try:
                self.conn = sql.connect("./db/mxsoftware.db")
                self.c = self.conn.cursor() 
                self.c.execute("INSERT INTO ogrenciler VALUES (?,?,?,?,?,?)",(tc,isim_soyad,numara,brans,kayit,bitis))
                self.conn.commit()
                self.c.close()
                self.conn.close()
                self.ui.statusBar.showMessage("Kayıt Başarılı",5000)
                self.btnTemizle()
                self.btnListeleClick()
            except Exception as error:
                self.ui.statusBar.showMessage("Kayıt Başarısız"+str(error),5000)
        else:
            self.ui.statusBar.showMessage("Alanlar Boş olamaz...",5000)



########################### EXPORT DATA ####################################

    def exportToExcelOgr(self):
        try:
            columnHeaders = []
            for j in range(self.ui.ogrenciler_tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.ogrenciler_tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.ogrenciler_tableWidget.rowCount()):
                for col in range(self.ui.ogrenciler_tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.ogrenciler_tableWidget.item(row, col).text()
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
            df.to_excel("Ogrenciler.xlsx", index=False)
            self.ui.statusBar.showMessage("Excel Dosyanız Hazırlandı (Masaüstü)",9000)
        except Exception as error:
            self.ui.statusBar.showMessage("Ogrenciler.xlsx Export Edilirken Hata İle Karşılaştık..."+str(error),5000)
    def exportToExcelAidat(self):
        try:
            columnHeaders = []
            for j in range(self.ui.aidatlar_tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.aidatlar_tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.aidatlar_tableWidget.rowCount()):
                for col in range(self.ui.aidatlar_tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.aidatlar_tableWidget.item(row, col).text()
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
            df.to_excel("Aidatlar.xlsx", index=False)
            self.ui.statusBar.showMessage("Excel Dosyanız Hazırlandı (Masaüstü)",9000)
        except Exception as error:
            self.ui.statusBar.showMessage("Aidatlar.xlsx Export Edilirken Hata İle Karşılaştık..."+str(error),5000)