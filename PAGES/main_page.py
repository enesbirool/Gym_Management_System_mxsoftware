from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem 
from PAGES.main_python import Ui_MainWindow
from PAGES.app_info import AppInfoPage
from PAGES.aidat_add import AidatAdd
from PyQt5.QtWidgets import QMessageBox
from assets.comments import *
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
        self.aidat_add_page=AidatAdd()

        self.ui.actionApp_info.triggered.connect(self.open_app_info_page)                    
        self.ui.ogr_export_button.hide()
        self.ui.aidat_export_button.hide()
        self.ui.actionExport_Data.toggled[bool].connect(self.btnstate)
        self.ui.register_button.clicked.connect(self.student_add)
        self.ui.delete_button.clicked.connect(self.btnSilClick)
        self.ui.ogrenciler_tableWidget.itemSelectionChanged.connect(self.ListOnClick)
        self.ui.ogr_export_button.clicked.connect(self.exportToExcelOgr) 
        self.ui.aidat_export_button.clicked.connect(self.exportToExcelAidat)
        self.ui.aidat_add_button.clicked.connect(self.open_aidat_page)
        self.ui.update_button.clicked.connect(self.btnUpdate)

##################### SUPPORTS #############################################       

    def btnstate(self,state):
        if (state==True):
            self.ui.ogr_export_button.show()
            self.ui.aidat_export_button.show()
            self.ui.statusBar.showMessage(export_buttons_showed,5000)
        else:
            self.ui.ogr_export_button.hide()
            self.ui.aidat_export_button.hide()
            self.ui.statusBar.showMessage(export_buttons_hide,5000)

    def btnTemizle(self):
        self.ui.ogr_tc_edit.clear()
        self.ui.ogr_name_surname_edit.clear()
        self.ui.ogr_number_edit.clear()
        self.ui.register_edit.clear()
        self.ui.register_finish_edit.clear()

    def closeEvent(self,event):
        reply = QMessageBox.question(self, close_window_header, close_window_event_commment,
			QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            self.ui.statusBar.showMessage(close_window_cancel,5000)
    def open_app_info_page(self):
        self.info_page.show()
    def open_aidat_page(self):
        self.aidat_add_page.show()


################################# CRUD OPERATIONS #############################

    def btnListeleClick(self): 
        self.ui.ogrenciler_tableWidget.clear()
        self.ui.ogrenciler_tableWidget.setColumnCount(6)
        self.ui.ogrenciler_tableWidget.setHorizontalHeaderLabels(('TC','Ad Soyad','Numara','Brans','Kayit','Bitis'))
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

    def ListOnClick(self): 
        self.ui.ogr_tc_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 0).text())
        self.ui.ogr_name_surname_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 1).text())
        self.ui.ogr_number_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 2).text())
        self.ui.brans_combox.setCurrentText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 3).text())
        self.ui.register_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 4).text())
        self.ui.register_finish_edit.setText(self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 5).text())
        

    def btnUpdate(self):
        tc=self.ui.ogr_tc_edit.text()
        isim_soyad=self.ui.ogr_name_surname_edit.text()
        numara=self.ui.ogr_number_edit.text()
        brans =self.ui.brans_combox.currentText()
        kayit=self.ui.register_edit.text()
        bitis=self.ui.register_finish_edit.text()
        if(len(tc)!=0):
            reply = QMessageBox.question(self, student_update_window_header, update_info_window+isim_soyad,
			QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    self.conn = sql.connect("./db/mxsoftware.db")
                    self.c = self.conn.cursor() 
                    self.c.execute("UPDATE ogrenciler SET  isim_soyad = ?, telefon = ?, \
                brans = ?, kayit_tarihi = ?, bitis_tarihi = ? WHERE tc = ?",(isim_soyad,numara,brans,kayit,bitis,tc))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.ui.statusBar.showMessage(isim_soyad+update_accept_student,6000)              
                except Exception:
                    print('Error', could_not_update_student)
                self.btnListeleClick()
                self.btnTemizle()
            else:
                self.ui.statusBar.showMessage(cancel_update_student,5000)
        else:
            self.ui.statusBar.showMessage(select_student_for_update,5000)
          
    def btnSilClick(self): 
        id = self.ui.ogr_tc_edit.text()
        isim_soyad= self.ui.ogr_name_surname_edit.text() 
        if  len(id)!=0:
            reply = QMessageBox.question(self, student_delete_window_header, delete_info_window+isim_soyad,
			QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    self.conn = sql.connect("./db/mxsoftware.db")
                    self.c = self.conn.cursor() 
                    self.c.execute('DELETE FROM ogrenciler WHERE tc = ?  ', (id,))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.ui.statusBar.showMessage(isim_soyad+delete_accept_student,6000)              
                except Exception:
                    print('Error', could_not_delete_student)
                self.btnListeleClick()
                self.btnTemizle()
            else:
                self.ui.statusBar.showMessage(cancel_delete_student,5000)
        else:            
            self.ui.statusBar.showMessage(select_student_for_delete,5000)
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
                self.ui.statusBar.showMessage(register_accept,5000)
                self.btnTemizle()
                self.btnListeleClick()
            except Exception as error:
                self.ui.statusBar.showMessage(register_error+str(error),5000)
        else:
            self.ui.statusBar.showMessage(ogr_can_not_be_null_error,5000)



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
            df.to_excel(ogrenciler_export_file, index=False)
            self.ui.statusBar.showMessage(ogrenciler_export_accept_status,9000)
        except Exception as error:
            self.ui.statusBar.showMessage(ogrenciler_export_error_status+str(error),5000)
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
            df.to_excel(aidatlar_export_file, index=False)
            self.ui.statusBar.showMessage(aidatlar_export_accept_status,9000)
        except Exception as error:
            self.ui.statusBar.showMessage(aidatlar_export_error_status+str(error),5000)