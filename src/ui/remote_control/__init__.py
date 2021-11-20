from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.utils import qrcode

from .view_model import RemoteControlViewModel
from .window import Ui_RemoteControlWindow


class RemoteControlWindow(QMainWindow, Ui_RemoteControlWindow):
    __view_model: RemoteControlViewModel

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = RemoteControlViewModel()

    def generate_qr_code(self, text: str):
        pixmap = qrcode.make_pixmap(text)
        self.qr_code_label.setPixmap(pixmap)
        self.setFixedSize(pixmap.size())

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        address = self.__view_model.start_api()
        self.generate_qr_code(address)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.__view_model.remote_api.stop()
