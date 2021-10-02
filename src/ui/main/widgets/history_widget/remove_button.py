import qtawesome as qta
from PyQt5 import QtCore, QtGui, QtWidgets


class RemoveButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setIcon(qta.icon('fa5s.times', color='#AAA'))
        self.setIconSize(QtCore.QSize(20, 20))
        self.setMaximumSize(QtCore.QSize(32, 32))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet('''
            background-color: transparent;
        ''')

        self.installEventFilter(self)

    def eventFilter(self, object: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.HoverEnter:
            self.setIcon(qta.icon('fa5s.times', color='#EC0059'))
        elif event.type() == QtCore.QEvent.HoverLeave:
            self.setIcon(qta.icon('fa5s.times', color='#AAA'))
        return super().eventFilter(object, event)
