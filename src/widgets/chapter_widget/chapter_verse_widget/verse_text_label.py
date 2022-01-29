from PyQt5 import QtWidgets
from src.utils import styles


class VerseTextLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWordWrap(True)
        self.setMaximumHeight(48)
        self.setMinimumHeight(48)
        self.unselect()

    def select(self):
        self.setStyleSheet(f"""
            color: {styles.qss_vars['@selectedVerseTextColor']};
            font-size: 12px;
            font-weight: bold;
        """)

    def unselect(self):
        self.setStyleSheet(f"""
            color: {styles.qss_vars['@textColor']};
            font-size: 12px;
            font-weight: unset;
        """)
