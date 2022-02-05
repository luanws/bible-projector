from PyQt5 import QtWidgets
from src.utils import styles
from src.utils.settings.theme_settings import ThemeSettings


class VerseTextLabel(QtWidgets.QLabel):
    __is_selected: bool
    theme_settings: ThemeSettings

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__is_selected = False
        self.theme_settings = ThemeSettings()

        self.setWordWrap(True)
        self.setMaximumHeight(48)
        self.setMinimumHeight(48)
        self.unselect()
        self.theme_settings.add_settings_listener(self.apply_styles)

    def apply_styles(self):
        try:
            if self.__is_selected:
                self.select()
            else:
                self.unselect()
        except RuntimeError:
            self.theme_settings.remove_settings_listener()

    def select(self):
        self.__is_selected = True
        self.setStyleSheet(f"""
            color: {styles.qss_vars['@selectedVerseTextColor']};
            font-size: 12px;
            font-weight: bold;
        """)

    def unselect(self):
        self.__is_selected = False
        self.setStyleSheet(f"""
            color: {styles.qss_vars['@textColor']};
            font-size: 12px;
            font-weight: unset;
        """)
