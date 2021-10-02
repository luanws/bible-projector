from PyQt5 import QtWidgets


class Container(QtWidgets.QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setContentsMargins(8, 8, 8, 8)
