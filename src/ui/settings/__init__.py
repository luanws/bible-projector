from PyQt5.QtWidgets import QMainWindow
from src.ui.settings.view_model import SettingsViewModel
from src.ui.settings.window import Ui_MainWindow


class SettingsWindow(QMainWindow, Ui_MainWindow):
    __view_model: SettingsViewModel

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.__view_model = SettingsViewModel()

        self.apply_button.clicked.connect(self.on_click_apply)
        self.font_size_spin_box.valueChanged.connect(self.on_change_font_size)

        self.configure_start_values()

    @property
    def view_model(self) -> SettingsViewModel:
        return self.__view_model

    def configure_start_values(self):
        font_size = self.view_model.projector_font_settings.font_size
        self.font_size_spin_box.setValue(font_size)

    def on_click_apply(self):
        self.view_model.save_settings()

    def on_change_font_size(self):
        font_size = self.font_size_spin_box.value()
        self.view_model.projector_font_settings.font_size = font_size
