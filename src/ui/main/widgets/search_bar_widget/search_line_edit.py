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

        self.configure_events()

    def configure_events(self):
        self.returnPressed.connect(self.search_callable)

    def request_focus(self):
        self.setFocus(True)
        self.selectAll()
