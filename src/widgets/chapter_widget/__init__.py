from typing import Callable, List, Optional

from PyQt5 import QtWidgets
from src.models.verse import Verse

from .chapter_verse_widget import ChapterVerseWidget


class ChapterWidget(QtWidgets.QWidget):
    __chapter: Optional[List[Verse]] = None
    chapter_verse_widgets: List[ChapterVerseWidget]
    list_widget: QtWidgets.QListWidget
    on_click_verse_callable: Optional[Callable[[Verse], None]] = None

    def __init__(
        self, parent=None, *,
        list_widget: QtWidgets.QListWidget,
        on_click: Optional[Callable[[Verse], None]] = None
    ):
        super(ChapterWidget, self).__init__(parent)

        self.list_widget = list_widget
        self.on_click_verse_callable = on_click

    @property
    def chapter(self) -> Optional[List[Verse]]:
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: List[Verse]):
        self.__chapter = chapter
        self.render()

    def render(self):
        self.list_widget.clear()
        chapter_verse_widgets = []
        for verse in self.__chapter:
            list_widget_item = QtWidgets.QListWidgetItem(
                self.list_widget)
            chapter_verse_widget = ChapterVerseWidget(
                verse=verse,
                list_widget_item=list_widget_item,
                on_click=self.on_click_verse_callable,
            )
            list_widget_item.setSizeHint(chapter_verse_widget.sizeHint())
            self.list_widget.addItem(list_widget_item)
            self.list_widget.setItemWidget(
                list_widget_item, chapter_verse_widget)
            chapter_verse_widgets.append(chapter_verse_widget)
        self.chapter_verse_widgets = chapter_verse_widgets

    def select_verse(self, verse: Verse):
        if self.chapter_verse_widgets is not None:
            for chapter_verse_widget in self.chapter_verse_widgets:
                chapter_verse_widget.unselect()
                if chapter_verse_widget.verse == verse:
                    chapter_verse_widget.select()

    def scroll_to_verse(self, verse: Verse):
        if self.chapter_verse_widgets is not None:
            chapter_verse_widget = self.chapter_verse_widgets[verse.verse_number - 1]
            self.list_widget.scrollToItem(
                chapter_verse_widget.list_widget_item,
                QtWidgets.QAbstractItemView.PositionAtCenter
            )
