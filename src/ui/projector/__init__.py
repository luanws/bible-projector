from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMainWindow
from src.ui.projector.view_model import ProjectorViewModel
from src.ui.projector.window import Ui_MainWindow


class ProjectorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = ProjectorViewModel()
        self.__view_model.on_change_text(self.on_change_text)
        self.__view_model.font_settings.add_settings_listener(
            self.configure_text_label_styles)

        self.text_label.setText('')
        self.configure_text_label_styles()

    @property
    def text(self):
        return self.__view_model.text

    @text.setter
    def text(self, text: str):
        self.__view_model.text = text

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()

    def close(self) -> bool:
        if self.text_label.text():
            self.text_label.setText('')
            return False
        return super().close()

    def show(self) -> None:
        self.text_label.setText(self.text)
        return super().show()

    def on_change_text(self, text: str):
        self.text_label.setText(text)

    def configure_text_label_styles(self):
        font_settings = self.__view_model.font_settings
        self.text_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.text_label.setStyleSheet(f"""
            color: {font_settings.color};
            font-size: {font_settings.font_size}pt;
            font-family: '{font_settings.font_family}';
            padding: {font_settings.margin}px;
            border-image: url({font_settings.background_image_path}) 0 0 0 0 stretch stretch;
        """)
