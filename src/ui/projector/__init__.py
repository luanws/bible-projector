from PyQt5 import QtCore
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMainWindow
from src.ui.projector.view_model import ProjectorViewModel
from src.ui.projector.window import Ui_MainWindow


class ProjectorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.__view_model = ProjectorViewModel()
        self.__view_model.on_change_text(self.on_change_text)

        self.textLabel.setText('')
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

    def on_change_text(self, text: str):
        self.textLabel.setText(text)

    def configure_text_label_styles(self):
        font_settings = self.__view_model.font_settings
        self.textLabel.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel.setStyleSheet(f"""
            color: white;
            font-size: {font_settings.font_size}pt;
            font-family: '{font_settings.font_family}';
            margin: {font_settings.margin}px;
        """)
