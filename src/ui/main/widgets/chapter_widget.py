from PyQt5 import QtWidgets
from src.models.verse import Verse


class ChapterVerseWidget(QtWidgets.QWidget):
    verse: Verse
    list_widget_item: QtWidgets.QListWidgetItem
    list_widget: QtWidgets.QListWidget
    selected: bool

    def __init__(
        self, parent=None, *,
        verse: Verse,
        list_widget_item: QtWidgets.QListWidgetItem,
    ):
        super(ChapterVerseWidget, self).__init__(parent)

        self.list_widget_item = list_widget_item
        self.selected = False

        self.container = QtWidgets.QHBoxLayout()
        self.verse_label = QtWidgets.QLabel()
        self.verse_number_label = QtWidgets.QLabel()

        self.verse_label.setText(verse.text)
        self.verse_number_label.setText(str(verse.verse_number))

        self.container.addWidget(self.verse_number_label)
        self.container.addWidget(self.verse_label)
        self.setLayout(self.container)

        self.container.setContentsMargins(0, 0, 0, 8)
        self.verse_label.setWordWrap(True)
        self.verse_number_label.setFixedWidth(24)
        self.verse_number_label.setStyleSheet('''
            color: #000088;
        ''')

        self.verse_label.setStyleSheet('''
            font-size: 12px;
        ''')

    def select(self):
        if not self.selected:
            self.verse_label.setStyleSheet('''
                color: #004;
                font-size: 12px;
                font-weight: bold;
            ''')
            self.selected = True

    def unselect(self):
        if self.selected:
            self.verse_label.setStyleSheet('''
                color: black;
                font-size: 12px;
                font-weight: unset;
            ''')
            self.selected = False
