from PyQt5 import QtWidgets


class VerseNumberLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(24)
        self.setStyleSheet('''
            color: #000088;
        ''')
