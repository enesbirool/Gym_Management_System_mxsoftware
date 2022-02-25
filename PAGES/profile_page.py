from PyQt5.QtWidgets import *
from PAGES.profile_python import Ui_Form
import sqlite3 as sql
from assets.comments import *

class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.exit_butotn.clicked.connect(self.pencere_kapat)
        self.ui.update_pushButton.clicked.connect(self.details_update)
    def pencere_kapat(self):
        self.close()
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
        photo = "null"

        try:
            self.conn = sql.connect("./db/mxsoftware.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE ogrenciler SET  isim = ?,soyad = ?, telefon = ?, \
            brans = ?, kayit_tarihi = ?, bitis_tarihi = ? WHERE tc = ?",
                               (isim, soyad, numara, brans, kayit, bitis, tc))
            self.conn.commit()
            self.c.execute("UPDATE details SET  veli_name = ?,veli_number = ?, lisans_no = ?, \
                        photo = ?, hes_code = ?, mail = ?,belt_color=?,date_of_birth=? WHERE tc = ?",
                           (veli_adi, veli_numara, lisans, photo, hes, mail,kusak,dogum_tarihi, tc))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            self.detail_updated()
        except Exception:
            print('Error', could_not_update_student)
    def detail_updated(self):
        QMessageBox.question(self, 'İnfo Page', "Güncellendi",QMessageBox.Ok)