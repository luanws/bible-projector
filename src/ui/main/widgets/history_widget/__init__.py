from typing import List

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from src.models.verse import Verse

from .history_item_widget import HistoryItemWidget


class HistoryWidget(QtWidgets.QWidget):
    __history: List[Verse]
    list_widget: QtWidgets.QListWidget
    history_item_widgets: List[HistoryItemWidget]
    reference_clicked = pyqtSignal(Verse)
    remove_clicked = pyqtSignal(Verse)

    def __init__(self, parent=None, *, list_widget: QtWidgets.QListWidget):
        super(HistoryWidget, self).__init__(parent)

        self.__history = []
        self.history_item_widgets = []
        self.list_widget = list_widget

    @property
    def history(self) -> List[Verse]:
        return self.__history

    def on_remove(self, verse: Verse):
        self.remove_verse(verse)
        self.remove_clicked.emit(verse)

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
        for history_item_widget in self.history_item_widgets:
            history_item_widget.deleteLater()
        self.history_item_widgets = []
        for verse in self.history:
            list_widget_item = QtWidgets.QListWidgetItem(
                self.list_widget)
            history_item_widget = HistoryItemWidget(
                verse=verse,
                list_widget_item=list_widget_item,
            )
            history_item_widget.reference_clicked.connect(
                self.reference_clicked.emit)
            history_item_widget.remove_clicked.connect(self.on_remove)
            self.history_item_widgets.append(history_item_widget)
            list_widget_item.setSizeHint(history_item_widget.sizeHint())
            self.list_widget.addItem(list_widget_item)
            self.list_widget.setItemWidget(
                list_widget_item, history_item_widget)
