from typing import Callable, Optional
from PyQt5 import QtCore, QtGui, QtWidgets
from src.models.verse import Verse


class HistoryWidget(QtWidgets.QWidget):
    verse: Verse
    list_widget_item: QtWidgets.QListWidgetItem
    __on_click_callable: Optional[Callable[[Verse], None]]

    def __init__(
        self, parent=None, *,
        verse: Verse,
        list_widget_item: QtWidgets.QListWidgetItem,
        on_click: Optional[Callable[[Verse], None]] = None
    ):
        super(HistoryWidget, self).__init__(parent)

        self.verse = verse
        self.list_widget_item = list_widget_item
        self.__on_click_callable = on_click

        self.container = QtWidgets.QHBoxLayout()
        self.reference_button = QtWidgets.QPushButton()

        self.reference_button.setText(str(verse.reference))

        self.container.addWidget(self.reference_button)
        self.setLayout(self.container)

        self.configure_events()
        self.configure_stylesheets()

    def configure_events(self):
        self.reference_button.clicked.connect(self.on_reference_label_click)

    def on_reference_label_click(self):
        if self.__on_click_callable:
            self.__on_click_callable(self.verse)

    def configure_stylesheets(self):
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.container.setContentsMargins(0, 0, 0, 0)
        self.reference_button.setStyleSheet('''
            text-align: left;
            font-size: 12px;
            padding: 8px;
            height: 14px;
            background-color: transparent;
        ''')
