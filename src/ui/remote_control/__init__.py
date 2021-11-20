from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
from src.utils import qrcode

from .window import Ui_RemoteControlWindow


class RemoteControlWindow(QMainWindow, Ui_RemoteControlWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setFixedSize(self.minimumSize())

        self.generate_qr_code('Hello World')

    def generate_qr_code(self, text: str):
        pixmap = qrcode.make_pixmap(text)
        self.qr_code_label.setPixmap(pixmap)
