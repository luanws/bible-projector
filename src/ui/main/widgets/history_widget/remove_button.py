import qtawesome as qta
from PyQt5 import QtCore, QtWidgets


class RemoveButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setIcon(qta.icon('fa5s.times', color='#EC0059'))
        self.setIconSize(QtCore.QSize(20, 20))
        self.setMaximumSize(QtCore.QSize(32, 32))
        self.setStyleSheet('''
            border: none;
            background-color: transparent;
        ''')
