from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.ui.settings.view_model import SettingsViewModel
from src.ui.settings.window import Ui_MainWindow


class SettingsWindow(QMainWindow, Ui_MainWindow):
    __view_model: SettingsViewModel

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = SettingsViewModel()

        self.apply_button.clicked.connect(self.on_click_apply)
        self.font_size_spin_box.valueChanged.connect(self.on_change_font_size)
        self.margin_spin_box.valueChanged.connect(self.on_change_margin)
        self.font_family_combo_box.currentTextChanged.connect(
            self.on_change_font_family)
        self.preview_text_line_edit.textChanged.connect(
            self.on_change_preview_text)

        self.configure_start_values()
        self.update_preview_label()

    @property
    def view_model(self) -> SettingsViewModel:
        return self.__view_model

    def configure_start_values(self):
        font_size = self.view_model.projector_font_settings.font_size
        font_family = self.view_model.projector_font_settings.font_family
        margin = self.view_model.projector_font_settings.margin
        self.font_size_spin_box.setValue(font_size)
        self.font_family_combo_box.setCurrentText(font_family)
        self.margin_spin_box.setValue(margin)

    def update_preview_label(self):
        text: str = self.preview_text_line_edit.text()
        font_settings = self.view_model.projector_font_settings
        self.preview_label.setText(text)
        self.preview_label.setStyleSheet(f"""
            color: white;
            background-color: black;
            font-size: {font_settings.font_size}pt;
            font-family: '{font_settings.font_family}';
            padding: {font_settings.margin}px;
        """)

    def on_change_preview_text(self):
        self.update_preview_label()

    def on_click_apply(self):
        self.view_model.save_settings()

    def on_change_font_size(self):
        font_size = self.font_size_spin_box.value()
        self.view_model.projector_font_settings.font_size = font_size
        self.update_preview_label()

    def on_change_font_family(self):
        font_family = self.font_family_combo_box.currentText()
        self.view_model.projector_font_settings.font_family = font_family
        self.update_preview_label()

    def on_change_margin(self):
        margin = self.margin_spin_box.value()
        self.view_model.projector_font_settings.margin = margin
        self.update_preview_label()
