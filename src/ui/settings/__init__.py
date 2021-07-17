from PyQt5.QtWidgets import QMainWindow
from src.ui.settings.window import Ui_MainWindow


class SettingsWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
