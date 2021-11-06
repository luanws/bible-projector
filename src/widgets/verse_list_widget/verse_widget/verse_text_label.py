from PyQt5 import QtWidgets, QtCore


class VerseTextLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignTop)
        self.setStyleSheet('''
            font-size: 12px;
        ''')
