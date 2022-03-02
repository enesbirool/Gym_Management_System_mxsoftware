from datetime import date
from smtplib import SMTP

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PAGES.mail_python import Ui_Form
import yagmail
import sqlite3 as sql
class MailPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.mail_edit.hide()
        self.kullanici_mail=""
        self.kullanici_sifre=""
        self.ui.password_edit.hide()
        self.ui.baglan_pushbutton.hide()
        self.ui.logout_pushbutton.hide()
        self.gonderilecek_mailler=[]
        self.son_ay_getir()
        self.ui.baglanti_durumu_checkBox.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "background-color : red;"
                               "}")
        self.ui.herkese_button.clicked.connect(self.herkese_tiklandi)
        self.ui.login_open_button.toggled[bool].connect(self.login_lane)
        self.ui.baglan_pushbutton.clicked.connect(self.mail_baglan)
        self.ui.logout_pushbutton.clicked.connect(self.mail_logout)
        self.ui.gonder_button.clicked.connect(self.mail_gonder)
    def mail_logout(self):
        self.ui.baglanti_durumu_checkBox.setStyleSheet("QCheckBox::indicator"
                                                       "{"
                                                       "background-color : red;"
                                                       "}")
        self.ui.mail_edit.clear()
        self.ui.password_edit.clear()
    def mail_baglan(self):
        try:
            yag = yagmail.SMTP(self.ui.mail_edit.text(), self.ui.password_edit.text())
            yag.send(to="deneme@gmail.com", subject="Test", contents="Test")
            self.kullanici_mail=self.ui.mail_edit.text()
            self.kullanici_sifre=self.ui.password_edit.text()
            self.ui.baglanti_durumu_checkBox.setStyleSheet("QCheckBox::indicator"
                                                        "{"
                                                        "background-color : lightgreen;"
                                                        "}")

        except Exception:
            QMessageBox.question(self, 'İnfo Page', "Mail veya şifre hatalı...",
                                 QMessageBox.Ok)
            self.mail_logout()
    def login_lane(self,state):
        if state==True:
            self.ui.mail_edit.show()
            self.ui.password_edit.show()
            self.ui.baglan_pushbutton.show()
            self.ui.logout_pushbutton.show()
        else:
            self.ui.mail_edit.hide()
            self.ui.password_edit.hide()
            self.ui.baglan_pushbutton.hide()
            self.ui.logout_pushbutton.hide()
    def mail_gonder(self):
        if len(self.gonderilecek_mailler)!=0:
            basarili=0
            basarisiz=0
            konu=self.ui.konu_basligi_lineEdit.text()
            message=self.ui.message_textEdit.toPlainText()
            yag=yagmail.SMTP(self.kullanici_mail,self.kullanici_sifre)
            mail_metni="""
            Merhaba ,
            
            {}
            
            
            MXSoftware Uygulaması tarafından toplu mail olarak gönderilmiştir...            
            """.format(message)
            mail_konusu="{}".format(konu)
            QMessageBox.question(self, 'İnfo Page', "Mail Gönderimi Başladı lütfen birkaç saniye keyfinize bakın... \n İşlem Sonunda Bildirileceksiniz...",
                                 QMessageBox.Ok)
            for mail in self.gonderilecek_mailler:
                try:
                    yag.send(to=mail,subject=mail_konusu,contents=mail_metni)
                    self.ui.mail_sended_textBrowser.setTextColor(QtGui.QColor('#36e330'))
                    self.ui.mail_sended_textBrowser.append("{} Adresine Gönderildi".format(mail))
                    basarili+=1
                except Exception as error:
                    self.ui.mail_sended_textBrowser.setTextColor(QtGui.QColor('#db250d'))
                    self.ui.mail_sended_textBrowser.append("{} Adresine Gönderilemedi".format(mail))
                    basarisiz+=1
            yag.close()
            QMessageBox.question(self, 'İnfo Page', "Mail Gönderimi Tamamlandı {} Başarılı , {} Başarısız...".format(basarili,basarisiz),
                                 QMessageBox.Ok)
            self.ui.message_textEdit.clear()
            self.ui.konu_basligi_lineEdit.clear()
            basarisiz=0
            basarili=0
        else:
            print("hataaaaaaaaaaaaaaaaaaaa")
            self.mail_logout()
    def son_ay_getir(self):
        today=str(date.today())
        today.split("-")
        yil=today[0] + today[1] + today[2] + today[3]
        ay=today[5] + today[6]
        self.gonderilecek_mailler.clear()
        try:
            self.conn = sql.connect("./db/mxsoftware.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM details WHERE ay=? yıl=?", (ay, yil))
            self.conn.commit()
            veri = self.c.fetchall()
            print(yil)
            print(ay)
        except Exception :
            print("veri yok")

    def herkese_tiklandi(self):

        self.gonderilecek_mailler.clear()
        sayi=0
        self.ui.mail_sended_textBrowser.clear()
        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM details"
        cur.execute(selectquery)
        rows = cur.fetchall()
        for mail in rows:
            sayi+=1
            self.gonderilecek_mailler.append(mail[8])
        self.ui.kalan_mail_label.setText(str(sayi))