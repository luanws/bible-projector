from PyQt5 import QtWidgets
from src.utils import styles


class VerseNumberLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(24)
        self.setStyleSheet(f"""
            color: {styles.qss_vars['@verseNumberTextColor']};
        """)
