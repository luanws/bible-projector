from typing import Callable

from PyQt5 import QtWidgets


class VersionsComboBox(QtWidgets.QComboBox):
    def __init__(
        self, parent=None, *,
        on_change_current_version_callable: Callable[[str], None]
    ):
        super().__init__(parent)

        self.on_change_current_version_callable = on_change_current_version_callable

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )

        self.currentTextChanged.connect(self.on_change_current_version)

    def on_change_current_version(self):
        version = self.currentText()
        self.on_change_current_version_callable(version)
