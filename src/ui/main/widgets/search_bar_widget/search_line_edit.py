from typing import Callable

from PyQt5 import QtWidgets


class SearchLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None, *, search_callable: Callable[[], None]):
        super().__init__(parent)

        self.search_callable = search_callable

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

        self.configure_events()

    def configure_events(self):
        self.returnPressed.connect(self.search_callable)

    def request_focus(self):
        self.setFocus(True)
        self.selectAll()
