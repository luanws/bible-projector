from typing import Callable, List, Optional

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from src.models.verse import Verse

from .verse_widget import VerseWidget


class VerseListWidget(QtWidgets.QWidget):
    __verses: Optional[List[Verse]] = None
    verse_widgets: List[VerseWidget]
    list_widget: QtWidgets.QListWidget
    verse_clicked = pyqtSignal(Verse)

    def __init__(self, parent=None, *, list_widget: QtWidgets.QListWidget):
        super(VerseListWidget, self).__init__(parent)

        self.list_widget = list_widget

    @property
    def verses(self) -> Optional[List[Verse]]:
        return self.__verses

    @verses.setter
    def verses(self, verses: List[Verse]):
        self.__verses = verses
        self.render()

    def render(self):
        self.list_widget.clear()
        verse_widgets = []
        for verse in self.__verses:
            list_widget_item = QtWidgets.QListWidgetItem(
                self.list_widget)
            verse_widget = VerseWidget(
                verse=verse,
                list_widget_item=list_widget_item,
            )
            verse_widget.clicked.connect(self.on_verse_clicked)
            list_widget_item.setSizeHint(verse_widget.sizeHint())
            self.list_widget.addItem(list_widget_item)
            self.list_widget.setItemWidget(
                list_widget_item, verse_widget)
            verse_widgets.append(verse_widget)
        self.verse_widgets = verse_widgets

    def on_verse_clicked(self, verse: Verse):
        self.verse_clicked.emit(verse)
