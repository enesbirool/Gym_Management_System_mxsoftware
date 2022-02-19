from PyQt5.QtWidgets import QMainWindow
from PAGES.main_python import Ui_MainWindow
from PAGES.app_info import AppInfoPage
from PyQt5.QtWidgets import QMessageBox

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionApp_info.triggered.connect(self.open_app_info_page)
        self.info_page=AppInfoPage()
        self.ui.ogr_export_button.hide()
        self.ui.aidat_export_button.hide()
        self.ui.actionExport_Data.toggled[bool].connect(self.btnstate)

    def open_app_info_page(self):
        self.info_page.show()
    def btnstate(self,state):
        if (state==True):
            self.ui.ogr_export_button.show()
            self.ui.aidat_export_button.show()
        else:
            self.ui.ogr_export_button.hide()
            self.ui.aidat_export_button.hide()
    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Close The Window', 'Are you sure you want to close the window?',
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        