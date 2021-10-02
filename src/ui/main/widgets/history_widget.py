from typing import Callable, Optional

import qtawesome as qta
from PyQt5 import QtCore, QtGui, QtWidgets
from src.models.verse import Verse


class HistoryWidget(QtWidgets.QWidget):
    verse: Verse
    list_widget_item: QtWidgets.QListWidgetItem
    __on_reference_click_callable: Optional[Callable[[Verse], None]]
    __on_remove_click_callable: Optional[Callable[[Verse], None]]

    def __init__(
        self, parent=None, *,
        verse: Verse,
        list_widget_item: QtWidgets.QListWidgetItem,
        on_reference_click: Optional[Callable[[Verse], None]] = None,
        on_remove_click: Optional[Callable[[Verse], None]] = None
    ):
        super(HistoryWidget, self).__init__(parent)

        self.verse = verse
        self.list_widget_item = list_widget_item
        self.__on_reference_click_callable = on_reference_click
        self.__on_remove_click_callable = on_remove_click

        self.container = QtWidgets.QHBoxLayout()
        self.reference_button = QtWidgets.QPushButton()
        self.remove_button = QtWidgets.QPushButton()

        self.reference_button.setText(str(verse.reference))

        self.container.addWidget(self.reference_button)
        self.container.addWidget(self.remove_button)
        self.setLayout(self.container)

        self.configure_events()
        self.configure_stylesheets()

    def configure_events(self):
        self.reference_button.clicked.connect(self.on_reference_button_click)
        self.remove_button.clicked.connect(self.on_remove_button_click)

    def on_remove_button_click(self):
        if self.__on_remove_click_callable:
            self.__on_remove_click_callable(self.verse)

    def on_reference_button_click(self):
        if self.__on_reference_click_callable:
            self.__on_reference_click_callable(self.verse)

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

        self.remove_button.setIcon(qta.icon('fa5s.times', color='#EC0059'))
        self.remove_button.setIconSize(QtCore.QSize(20, 20))
        self.remove_button.setMaximumSize(QtCore.QSize(32, 32))
        self.remove_button.setStyleSheet('''
            border: none;
            background-color: transparent;
        ''')
