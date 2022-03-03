from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PAGES.profile_python import Ui_Form
import sqlite3 as sql
from assets.comments import *

class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.update_pushButton.clicked.connect(self.details_update)
        self.ui.pick_photo_button.clicked.connect(self.browse_photo)


    def conver_image_into_binary(self,filename):
        with open(filename, 'rb') as file:
            photo_image = file.read()
        return photo_image
    def pp_update(self):
        pixmap = QtGui.QPixmap()
        tc = self.ui.tc_edit.text()
        self.conn = sql.connect("./db/mxsoftware.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM details WHERE tc=? OR (tc=? AND tc=?) OR tc=? ",
                       (tc, tc, tc, tc))
        self.conn.commit()
        for i in self.c:
            pixmap.loadFromData(i[6], 'png')
            self.ui.photo_label.clear()
            self.ui.photo_label.setPixmap(pixmap)
    def browse_photo(self):
        try:
            tc=self.ui.tc_edit.text()
            binary=""
            self.fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:/',"Select Photo (*.png *.jpg *.PNG *.JPG)")
            with open(self.fname[0], 'rb') as file:
                photo_image = file.read()
                binary=photo_image
            self.conn = sql.connect("./db/mxsoftware.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE details SET  photo = ? WHERE tc = ?",
                           (binary, tc))
            self.conn.commit()
            self.conn.close()
            self.pp_update()


            binary=""
        except Exception:
            print("arıza")

    def details_update(self):
        tc=self.ui.tc_edit.text()
        isim = self.ui.isim_edit.text().upper()
        soyad = self.ui.soyad_edit.text().upper()
        numara = self.ui.phone_edit.text()
        brans = self.ui.brans_comboBox.currentText()
        kayit = self.ui.register_edit.text()
        bitis = self.ui.register_finish_edit.text()
        veli_adi = self.ui.veli_name_edit.text().upper()
        veli_numara = self.ui.veli_phone_edit.text()
        lisans = self.ui.lisans_no_edit.text()
        dogum_tarihi = self.ui.date_of_birth_edit.text()
        hes = self.ui.hes_code_edit.text()
        kusak = self.ui.kusak_edit.text()
        mail = self.ui.mail_edit.text()
        photo = ""


        try:
            self.conn = sql.connect("./db/mxsoftware.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE ogrenciler SET  isim = ?,soyad = ?, telefon = ?, \
            brans = ?, kayit_tarihi = ?, bitis_tarihi = ? WHERE tc = ?",
                               (isim, soyad, numara, brans, kayit, bitis, tc))
            self.conn.commit()
            self.c.execute("UPDATE details SET  veli_name = ?,veli_number = ?, lisans_no = ?, hes_code = ?, mail = ?,belt_color=?,date_of_birth=? WHERE tc = ?",
                           (veli_adi, veli_numara, lisans, hes, mail,kusak,dogum_tarihi, tc))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            self.detail_updated()
        except Exception:
            print('Error', could_not_update_student)
    def detail_updated(self):
        QMessageBox.question(self, 'İnfo Page', "Güncellendi",QMessageBox.Ok)
    def detail_ui_clear(self):
        self.ui.tc_edit.clear()
        self.ui.isim_edit.clear()
        self.ui.soyad_edit.clear()
        self.ui.phone_edit.clear()
        self.ui.register_edit.clear()
        self.ui.register_finish_edit.clear()
        self.ui.veli_name_edit.clear()
        self.ui.veli_phone_edit.clear()
        self.ui.lisans_no_edit.clear()
        self.ui.photo_label.clear()
        self.ui.date_of_birth_edit.clear()
        self.ui.hes_code_edit.clear()
        self.ui.kusak_edit.clear()
        self.ui.mail_edit.clear()
        self.ui.veli_name_edit.clear()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, close_window_header, close_window_event_commment,
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            self.detail_ui_clear()