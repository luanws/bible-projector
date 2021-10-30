from PyQt5 import QtWidgets


class VerseTextLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWordWrap(True)
        self.setMaximumHeight(48)
        self.setMinimumHeight(48)
        self.setStyleSheet('''
            font-size: 12px;
            background-color: transparent;
        ''')

    def select(self):
        self.setStyleSheet('''
            color: #004;
            font-size: 12px;
            font-weight: bold;
            background-color: transparent;
        ''')
    
    def unselect(self):
        self.setStyleSheet('''
            color: black;
            font-size: 12px;
            font-weight: unset;
            background-color: transparent;
        ''')
