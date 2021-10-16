from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

from .window import Ui_MainWindow


class AdvancedSearchWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        