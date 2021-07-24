from PyQt5 import QtWidgets
from src.models.verse import Verse


class ChapterWidget (QtWidgets.QWidget):
    def __init__(self, parent=None, *, verse: Verse):
        super(ChapterWidget, self).__init__(parent)
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
