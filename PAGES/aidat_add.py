from PyQt5.QtWidgets import *
from PAGES.aidat_add_python import Ui_Form
import sqlite3 as sql
from assets.comments import *

class AidatAdd(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.combo_ekle()
        self.ui.pushButton.clicked.connect(self.open_info)
    def open_info(self):
        QMessageBox.question(self, 'İnfo Page', info_page_comment,
			QMessageBox.Ok)

    def combo_ekle(self):
        isimler=[]

        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM ogrenciler"
        cur.execute(selectquery)
        rows=cur.fetchall()
        for isim in rows:
            isimler.append(str(isim[1]))
        self.ui.aidat_comboBox.addItems(isimler)

        