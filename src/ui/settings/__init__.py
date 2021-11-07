from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QColorDialog, QMainWindow
from src.ui.settings.view_model import SettingsViewModel
from src.ui.settings.window import Ui_MainWindow
from src.widgets.outlined_label import OutlinedLabel


def q_color_to_hex(color: QtGui.QColor) -> str:
    return f'#{color.red():02x}{color.green():02x}{color.blue():02x}'


class SettingsWindow(QMainWindow, Ui_MainWindow):
    __view_model: SettingsViewModel

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = SettingsViewModel()
        self.preview_label = OutlinedLabel(1/16)
        self.preview_label.setWordWrap(True)
        self.preview_label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.vertical_layout.addWidget(self.preview_label)

        self.update_preview_label()
        self.configure_events()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.__view_model.reset_projector_font_settings()
        self.configure_start_values()
        return super().showEvent(a0)

    def configure_events(self):
        self.apply_button.clicked.connect(self.on_click_apply)
        self.font_size_spin_box.valueChanged.connect(self.on_change_font_size)
        self.margin_spin_box.valueChanged.connect(self.on_change_margin)
        self.font_family_combo_box.currentTextChanged.connect(
            self.on_change_font_family)
        self.preview_text_line_edit.textChanged.connect(
            self.on_change_preview_text)
        self.change_color_button.clicked.connect(
            self.on_click_change_color_button)
        self.preview_label.mousePressEvent = self.on_click_preview_label

    def configure_start_values(self):
        font_size = self.__view_model.projector_font_settings.font_size
        font_family = self.__view_model.projector_font_settings.font_family
        margin = self.__view_model.projector_font_settings.margin
        color = self.__view_model.projector_font_settings.color
        self.font_size_spin_box.setValue(font_size)
        self.font_family_combo_box.setCurrentText(font_family)
        self.margin_spin_box.setValue(margin)
        self.change_color_button.setStyleSheet(f"""
            border-style: solid;
            border-radius: 2px;
            background-color: {color};
            border-color: black;
            border-width: 1px;
        """)

    def update_preview_label(self):
        text: str = self.preview_text_line_edit.text()
        font_settings = self.__view_model.projector_font_settings
        self.preview_label.setText(text)
        self.preview_label.setStyleSheet(f"""
            color: {font_settings.color};
            background-color: black;
            font-size: {font_settings.font_size}pt;
            font-family: '{font_settings.font_family}';
            padding: {font_settings.margin}px;
            border-image: url({font_settings.background_image_path}) 0 0 0 0 stretch stretch;
        """)

    def on_click_preview_label(self, event: QtGui.QMouseEvent):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Imagem de fundo",
            "",
            "Imagens (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        self.__view_model.projector_font_settings.background_image_path = file_path
        self.update_preview_label()

    def on_click_change_color_button(self):
        q_color = QColorDialog.getColor()
        color = q_color_to_hex(q_color)
        self.__view_model.projector_font_settings.color = color
        self.change_color_button.setStyleSheet(f"""
            border-style: solid;
            border-radius: 2px;
            background-color: {color};
            border-color: black;
            border-width: 1px;
        """)
        self.update_preview_label()

    def on_change_preview_text(self):
        self.update_preview_label()

    def on_click_apply(self):
        self.__view_model.save_settings()

    def on_change_font_size(self):
        font_size = self.font_size_spin_box.value()
        self.__view_model.projector_font_settings.font_size = font_size
        self.update_preview_label()

    def on_change_font_family(self):
        font_family = self.font_family_combo_box.currentText()
        self.__view_model.projector_font_settings.font_family = font_family
        self.update_preview_label()

    def on_change_margin(self):
        margin = self.margin_spin_box.value()
        self.__view_model.projector_font_settings.margin = margin
        self.update_preview_label()
