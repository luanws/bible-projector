from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal


class VersionsComboBox(QtWidgets.QComboBox):
    change_version = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )

        self.currentTextChanged.connect(self.on_change_current_version)

    def on_change_current_version(self):
        version = self.currentText()
        self.change_version.emit(version)
