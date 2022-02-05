from typing import Callable, Optional

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from src.models.verse import Verse
from src.ui.advanced_search.view_model import AdvancedSearchViewModel
from src.widgets.verse_list_widget import VerseListWidget

from .window import Ui_MainWindow


class AdvancedSearchWindow(QMainWindow, Ui_MainWindow):
    verse_list_widget: VerseListWidget
    __view_model: AdvancedSearchViewModel
    verse_clicked = pyqtSignal(Verse)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = AdvancedSearchViewModel()
        self.verse_list_widget = VerseListWidget(
            list_widget=self.chapter_list_widget,
        )
        self.books_combo_box.addItems(
            self.__view_model.get_all_book_options())

        self.configure_events()

    def show(self) -> None:
        self.__view_model.update_versions()
        self.versions_combo_box.clear()
        self.versions_combo_box.addItems(
            self.__view_model.get_all_version_options())
        return super().show()

    def configure_events(self):
        self.search_line_edit.returnPressed.connect(self.search)
        self.versions_combo_box.currentTextChanged.connect(
            self.on_change_version)
        self.books_combo_box.currentTextChanged.connect(
            self.on_change_book)
        self.verse_list_widget.verse_clicked.connect(self.on_verse_clicked)

    def on_change_version(self, version: str):
        self.search()

    def on_change_book(self, book: str):
        self.search()

    def on_verse_clicked(self, verse: Verse):
        self.verse_clicked.emit(verse)

    def search(self):
        search_text: str = self.search_line_edit.text()
        version = self.versions_combo_box.currentText()
        book = self.books_combo_box.currentText()
        verses = self.__view_model.search(search_text, book, version)
        self.verse_list_widget.verses = verses
