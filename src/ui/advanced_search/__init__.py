from typing import Callable, Optional

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.models.verse import Verse
from src.ui.advanced_search.view_model import AdvancedSearchViewModel
from src.widgets.verse_list_widget import VerseListWidget

from .window import Ui_MainWindow


class AdvancedSearchWindow(QMainWindow, Ui_MainWindow):
    chapter_widget: VerseListWidget
    __view_model: AdvancedSearchViewModel
    on_verse_clicked_callable: Optional[Callable[[Verse], None]]

    def __init__(self, on_verse_clicked: Callable[[Verse], None] = None):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.on_verse_clicked_callable = on_verse_clicked

        self.__view_model = AdvancedSearchViewModel()
        self.chapter_widget = VerseListWidget(
            list_widget=self.chapter_list_widget,
            on_click=self.on_verse_clicked
        )
        self.versions_combo_box.addItems(
            self.__view_model.get_all_version_options())
        self.books_combo_box.addItems(
            self.__view_model.get_all_book_options())

        self.configure_events()

    def configure_events(self):
        self.search_line_edit.returnPressed.connect(self.search)
        self.versions_combo_box.currentTextChanged.connect(
            self.on_change_version)
        self.books_combo_box.currentTextChanged.connect(
            self.on_change_book)

    def on_change_version(self, version: str):
        self.search()

    def on_change_book(self, book: str):
        self.search()

    def on_verse_clicked(self, verse: Verse):
        if self.on_verse_clicked_callable:
            self.on_verse_clicked_callable(verse)

    def search(self):
        search_text: str = self.search_line_edit.text()
        version = self.versions_combo_box.currentText()
        book = self.books_combo_box.currentText()
        verses = self.__view_model.search(search_text, book, version)
        self.chapter_widget.verses = verses
