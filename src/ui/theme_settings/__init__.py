from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.ui.theme_settings.view_model import ThemeSettingsViewModel
from src.ui.theme_settings.window import Ui_MainWindow


class ThemeSettingsWindow(QMainWindow, Ui_MainWindow):
    __view_model: ThemeSettingsViewModel

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = ThemeSettingsViewModel()

        self.configure_initial_values()
        self.configure_events()

    def configure_initial_values(self):
        self.themes_combo_box.addItems(self.__view_model.themes)
        self.themes_combo_box.setCurrentText(self.__view_model.current_theme)

    def configure_events(self):
        self.themes_combo_box.currentTextChanged.connect(
            self.on_change_theme)

    def on_change_theme(self):
        theme = self.themes_combo_box.currentText()
        self.__view_model.change_theme(theme)
