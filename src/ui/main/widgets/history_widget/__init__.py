from typing import Callable, List, Optional

from PyQt5 import QtWidgets
from src.models.verse import Verse

from .history_item_widget import HistoryItemWidget


class HistoryWidget(QtWidgets.QWidget):
    __history: List[Verse]
    list_widget: QtWidgets.QListWidget
    list_widget_item: QtWidgets.QListWidgetItem
    __on_reference_click_callable: Optional[Callable[[Verse], None]]
    __on_remove_click_callable: Optional[Callable[[Verse], None]]

    def __init__(
        self, parent=None, *,
        list_widget: QtWidgets.QListWidget,
        on_reference_click: Optional[Callable[[Verse], None]] = None,
        on_remove_click: Optional[Callable[[Verse], None]] = None
    ):
        super(HistoryWidget, self).__init__(parent)

        self.__history = []
        self.list_widget = list_widget
        self.__on_reference_click_callable = on_reference_click
        self.__on_remove_click_callable = on_remove_click

    @property
    def history(self) -> List[Verse]:
        return self.__history

    def on_remove(self, verse: Verse):
        self.remove_verse(verse)
        if self.__on_remove_click_callable:
            self.__on_remove_click_callable(verse)

    def add_verse(self, verse: Verse):
        if verse in self.history:
            self.__history.remove(verse)
        self.__history.append(verse)
        self.render()

    def remove_verse(self, verse: Verse):
        self.__history.remove(verse)
        self.render()

    def render(self):
        self.list_widget.clear()
        for verse in self.history:
            list_widget_item = QtWidgets.QListWidgetItem(
                self.list_widget)
            history_widget = HistoryItemWidget(
                verse=verse,
                list_widget_item=list_widget_item,
                on_reference_click=self.__on_reference_click_callable,
                on_remove_click=self.on_remove,
            )
            list_widget_item.setSizeHint(history_widget.sizeHint())
            self.list_widget.addItem(list_widget_item)
            self.list_widget.setItemWidget(
                list_widget_item, history_widget)
