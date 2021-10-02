from PyQt5 import QtWidgets


class VersionsComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )
        self.setStyleSheet("""
            QComboBox {
                border-style: solid;
                border-color: gray;
                border-width: 1px;
                border-radius: 3px;
                padding: 4px;
                background-color: rgb(220, 220, 220);
                color: black;
                width: 30px;
            }
        """)
