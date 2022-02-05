from typing import List, Optional

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from src.models.verse import Verse

from .chapter_verse_widget import ChapterVerseWidget


class ChapterWidget(QtWidgets.QWidget):
    __chapter: Optional[List[Verse]] = None
    chapter_verse_widgets: List[ChapterVerseWidget] = []
    list_widget: QtWidgets.QListWidget
    verse_clicked = pyqtSignal(Verse)

    def __init__(self, parent=None, *, list_widget: QtWidgets.QListWidget):
        super(ChapterWidget, self).__init__(parent)

        self.list_widget = list_widget

    @property
    def chapter(self) -> Optional[List[Verse]]:
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: List[Verse]):
        self.__chapter = chapter
        self.render()

    def get_chapter_verse_widget(self, verse: Verse) -> ChapterVerseWidget:
        list_widget_item = QtWidgets.QListWidgetItem(self.list_widget)
        chapter_verse_widget = ChapterVerseWidget(
            verse=verse,
            list_widget_item=list_widget_item,
        )
        chapter_verse_widget.clicked.connect(self.verse_clicked.emit)
        return chapter_verse_widget

    def render(self):
        self.list_widget.clear()
        self.chapter_verse_widgets = []

        for verse in self.__chapter:
            chapter_verse_widget = self.get_chapter_verse_widget(verse)
            self.chapter_verse_widgets.append(chapter_verse_widget)

        for chapter_verse_widget in self.chapter_verse_widgets:
            list_widget_item = chapter_verse_widget.list_widget_item
            self.list_widget.addItem(list_widget_item)
            self.list_widget.setItemWidget(
                list_widget_item, chapter_verse_widget)

    def select_verse(self, verse: Verse):
        if self.chapter_verse_widgets is not None:
            for chapter_verse_widget in self.chapter_verse_widgets:
                chapter_verse_widget.unselect()
                if chapter_verse_widget.verse == verse:
                    chapter_verse_widget.select()

    def scroll_to_verse(self, verse: Verse):
        if len(self.chapter_verse_widgets) > 0:
            chapter_verse_widget = self.chapter_verse_widgets[verse.verse_number - 1]
            self.list_widget.scrollToItem(
                chapter_verse_widget.list_widget_item,
                QtWidgets.QAbstractItemView.PositionAtCenter
            )
