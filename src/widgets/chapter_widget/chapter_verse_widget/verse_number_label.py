from PyQt5 import QtWidgets
from src.utils import styles
from src.utils.settings.theme_settings import ThemeSettings


class VerseNumberLabel(QtWidgets.QLabel):
    theme_settings: ThemeSettings

    def __init__(self, parent=None):
        super().__init__(parent)

        self.theme_settings = ThemeSettings()

        self.setFixedWidth(24)

        self.apply_styles()
        self.theme_settings.on_change_settings(self.apply_styles)

    def apply_styles(self):
        self.setStyleSheet(f"""
            color: {styles.qss_vars['@verseNumberTextColor']};
        """)
