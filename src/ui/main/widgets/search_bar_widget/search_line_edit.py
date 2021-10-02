from PyQt5 import QtWidgets


class SearchLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred
        )
        self.setPlaceholderText("Referência (F4)")
        self.setStyleSheet("""
            border-style: solid;
            border-color: gray;
            border-width: 1px;
            border-radius: 3px;
            padding: 3px;
            background-color: white;
            color: black;
        """)
