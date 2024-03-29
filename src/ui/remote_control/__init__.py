from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow

from src.ui.main.control import MainWindowControl
from src.utils import qrcode

from .view_model import RemoteControlViewModel
from .window import Ui_RemoteControlWindow


class RemoteControlWindow(QMainWindow, Ui_RemoteControlWindow):
    __view_model: RemoteControlViewModel
    main_window_control: MainWindowControl

    def __init__(self, parent=None, *, main_window_control: MainWindowControl):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = RemoteControlViewModel(main_window_control)

    def generate_qr_code(self, text: str):
        pixmap = qrcode.make_pixmap(text)
        self.qr_code_label.setPixmap(pixmap)
        self.qr_code_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setFixedSize(pixmap.size())

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        address = self.__view_model.start_api()
        self.generate_qr_code(address)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.__view_model.remote_api.stop()
