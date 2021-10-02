from typing import Optional

import qtawesome as qta
from PyQt5 import QtCore, QtGui, QtWidgets


class IconButton(QtWidgets.QPushButton):
    icon_name: str
    color: Optional[str]
    active_color: Optional[str]

    def __init__(self, icon_name: str, color: str = None, active_color: str = None, size: int = 20, parent=None):
        super().__init__(parent)

        self.icon_name = icon_name
        self.color = color
        self.active_color = active_color

        self.setIcon(qta.icon(self.icon_name, color=self.color))
        self.setIconSize(QtCore.QSize(size, size))
        self.setMaximumSize(QtCore.QSize(32, 32))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet('''
            background-color: transparent;
        ''')

        self.installEventFilter(self)

    def eventFilter(self, object: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.HoverEnter:
            self.setIcon(qta.icon(self.icon_name, color=self.active_color))
        elif event.type() == QtCore.QEvent.HoverLeave:
            self.setIcon(qta.icon(self.icon_name, color=self.color))
        return super().eventFilter(object, event)
