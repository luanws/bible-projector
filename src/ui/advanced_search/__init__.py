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

        self.configure_events()

    def configure_events(self):
        self.search_line_edit.returnPressed.connect(self.search)

    def search(self):
        search_text: str = self.search_line_edit.text()
        verses = self.__view_model.search(search_text)
        self.chapter_widget.verses = verses
