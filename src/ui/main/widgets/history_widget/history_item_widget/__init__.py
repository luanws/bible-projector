from typing import Callable, Optional

from PyQt5 import QtWidgets
from src.models.verse import Verse
from src.utils import styles

from .container import Container
from .reference_button import ReferenceButton
from .remove_button import RemoveButton


class HistoryItemWidget(QtWidgets.QWidget):
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
        super(HistoryItemWidget, self).__init__(parent)

        self.verse = verse
        self.list_widget_item = list_widget_item
        self.__on_reference_click_callable = on_reference_click
        self.__on_remove_click_callable = on_remove_click

        self.container = Container()
        self.reference_button = ReferenceButton()
        self.remove_button = RemoveButton()

        self.reference_button.setText(str(verse.reference))

        self.container.addWidget(self.reference_button)
        self.container.addWidget(self.remove_button)
        self.setLayout(self.container)

        self.setStyleSheet(styles.get_qss_stylesheet('src/ui/main/widgets/history_widget/history_item_widget/styles.qss'))
        self.configure_events()

    def configure_events(self):
        self.reference_button.clicked.connect(self.on_reference_button_click)
        self.remove_button.clicked.connect(self.on_remove_button_click)

    def on_remove_button_click(self):
        if self.__on_remove_click_callable:
            self.__on_remove_click_callable(self.verse)

    def on_reference_button_click(self):
        if self.__on_reference_click_callable:
            self.__on_reference_click_callable(self.verse)
