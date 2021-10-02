from PyQt5 import QtCore, QtGui, QtWidgets


class ReferenceButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet('''
            text-align: left;
            font-size: 12px;
            padding: 8px;
            height: 14px;
            background-color: transparent;
        ''')
