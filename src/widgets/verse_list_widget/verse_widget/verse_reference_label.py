from PyQt5 import QtCore, QtWidgets


class VerseReferenceLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAlignment(QtCore.Qt.AlignBottom)
        self.setStyleSheet('''
            color: #000088;
        ''')
