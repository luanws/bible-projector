from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.ui.advanced_search.view_model import AdvancedSearchViewModel
from src.widgets.verse_list_widget import VerseListWidget

from .window import Ui_MainWindow


class AdvancedSearchWindow(QMainWindow, Ui_MainWindow):
    chapter_widget: VerseListWidget
    __view_model: AdvancedSearchViewModel

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = AdvancedSearchViewModel()
        self.chapter_widget = VerseListWidget(
            list_widget=self.chapter_list_widget,
        )
        self.versions_combo_box.addItems(
            self.__view_model.get_version_options())

        self.configure_events()

    def configure_events(self):
        self.search_line_edit.returnPressed.connect(self.search)
        self.versions_combo_box.currentTextChanged.connect(
            self.on_change_version)

    def on_change_version(self, version: str):
        self.search()

    def search(self):
        search_text: str = self.search_line_edit.text()
        version = self.versions_combo_box.currentText()
        verses = self.__view_model.search(search_text, version)
        self.chapter_widget.verses = verses
