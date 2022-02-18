from PyQt5.QtWidgets import QMainWindow
from main_python import Ui_MainWindow
from qt_material import apply_stylesheet

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)