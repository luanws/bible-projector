from typing import Callable, Optional

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from src.models.verse import Verse

from .container import Container
from .verse_number_label import VerseNumberLabel
from .verse_text_label import VerseTextLabel


class ChapterVerseWidget(QtWidgets.QWidget):
    verse: Verse
    list_widget_item: QtWidgets.QListWidgetItem
    list_widget: QtWidgets.QListWidget
    __selected: bool
    clicked = pyqtSignal(Verse)

    def __init__(
        self, parent=None, *,
        verse: Verse,
        list_widget_item: QtWidgets.QListWidgetItem,
    ):
        super(ChapterVerseWidget, self).__init__(parent)

        self.verse = verse
        self.list_widget_item = list_widget_item
        self.__selected = False

        self.container = Container()
        self.verse_text_label = VerseTextLabel()
        self.verse_number_label = VerseNumberLabel()

        self.verse_text_label.setText(verse.text)
        self.verse_number_label.setText(str(verse.verse_number))

        self.container.addWidget(self.verse_number_label)
        self.container.addWidget(self.verse_text_label)
        self.setLayout(self.container)

        list_widget_item.setSizeHint(self.sizeHint())

        self.configure_events()

    def configure_events(self):
        self.mouseReleaseEvent = self.__on_click

    def __on_click(self, event: QtGui.QMouseEvent):
        self.clicked.emit(self.verse)

    def select(self):
        if not self.__selected:
            self.verse_text_label.select()
            self.__selected = True

    def unselect(self):
        if self.__selected:
            self.verse_text_label.unselect()
            self.__selected = False
