from typing import Callable, Optional

from PyQt5 import QtGui, QtWidgets
from src.models.verse import Verse

from .container import Container
from .verse_reference_label import VerseReferenceLabel
from .verse_text_label import VerseTextLabel


class VerseWidget(QtWidgets.QWidget):
    verse: Verse
    list_widget_item: QtWidgets.QListWidgetItem
    list_widget: QtWidgets.QListWidget
    __on_click_callable: Optional[Callable[[Verse], None]]

    def __init__(
        self, parent=None, *,
        verse: Verse,
        list_widget_item: QtWidgets.QListWidgetItem,
        on_click: Optional[Callable[[Verse], None]] = None
    ):
        super(VerseWidget, self).__init__(parent)

        self.verse = verse
        self.list_widget_item = list_widget_item
        self.__on_click_callable = on_click

        self.container = Container()
        self.verse_text_label = VerseTextLabel()
        self.verse_reference_label = VerseReferenceLabel()

        self.verse_text_label.setText(verse.text)
        reference = str(verse.reference) + ' ' + verse.version.version
        self.verse_reference_label.setText(reference)

        self.container.addWidget(self.verse_reference_label)
        self.container.addWidget(self.verse_text_label)
        self.setLayout(self.container)

        self.configure_events()

    def configure_events(self):
        self.mouseReleaseEvent = self.__on_click

    def __on_click(self, event: QtGui.QMouseEvent):
        if self.__on_click_callable:
            self.__on_click_callable(self.verse)
