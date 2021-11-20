from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

from .window import Ui_RemoteControlWindow


class RemoteControlWindow(QMainWindow, Ui_RemoteControlWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))
