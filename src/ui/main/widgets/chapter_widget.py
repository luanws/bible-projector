from typing import Callable, Optional

from PyQt5 import QtGui, QtWidgets
from src.models.verse import Verse


class ChapterVerseWidget(QtWidgets.QWidget):
    verse: Verse
    list_widget_item: QtWidgets.QListWidgetItem
    list_widget: QtWidgets.QListWidget
    __on_click_callable: Optional[Callable[[Verse], None]]
    __selected: bool

    def __init__(
        self, parent=None, *,
        verse: Verse,
        list_widget_item: QtWidgets.QListWidgetItem,
        on_click: Optional[Callable[[Verse], None]] = None
    ):
        super(ChapterVerseWidget, self).__init__(parent)

        self.verse = verse
        self.list_widget_item = list_widget_item
        self.__on_click_callable = on_click
        self.__selected = False

        self.container = QtWidgets.QHBoxLayout()
        self.verse_label = QtWidgets.QLabel()
        self.verse_number_label = QtWidgets.QLabel()

        self.verse_label.setText(verse.text)
        self.verse_number_label.setText(str(verse.verse_number))

        self.container.addWidget(self.verse_number_label)
        self.container.addWidget(self.verse_label)
        self.setLayout(self.container)

        self.configure_events()
        self.configure_stylesheets()

    def configure_events(self):
        self.mouseReleaseEvent = self.__on_click

    def configure_stylesheets(self):
        self.container.setContentsMargins(8, 8, 8, 8)

        self.verse_number_label.setFixedWidth(24)
        self.verse_number_label.setStyleSheet('''
            color: #000088;
        ''')

        self.verse_label.setWordWrap(True)
        self.verse_label.setMaximumHeight(48)
        self.verse_label.setMinimumHeight(48)
        self.verse_label.setStyleSheet('''
            font-size: 12px;
        ''')

    def __on_click(self, event: QtGui.QMouseEvent):
        if self.__on_click_callable:
            self.__on_click_callable(self.verse)

    def select(self):
        if not self.__selected:
            self.verse_label.setStyleSheet('''
                color: #004;
                font-size: 12px;
                font-weight: bold;
            ''')
            self.__selected = True

    def unselect(self):
        if self.__selected:
            self.verse_label.setStyleSheet('''
                color: black;
                font-size: 12px;
                font-weight: unset;
            ''')
            self.__selected = False
