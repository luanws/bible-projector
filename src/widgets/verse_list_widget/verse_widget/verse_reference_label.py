from PyQt5 import QtCore, QtWidgets
from src.utils import styles


class VerseReferenceLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAlignment(QtCore.Qt.AlignBottom)
        self.setStyleSheet(f"""
            font-weight: bold;
            color: {styles.qss_vars['@verseReferenceTextColor']};
        """)
