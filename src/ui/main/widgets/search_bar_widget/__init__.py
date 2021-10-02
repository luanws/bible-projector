from PyQt5 import QtWidgets
from src import widgets

from .container import Container
from .search_line_edit import SearchLineEdit
from .versions_combo_box import VersionsComboBox


class SearchBarWidget(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super(SearchBarWidget, self).__init__(parent)

        self.container = Container()
        self.versions_combo_box = VersionsComboBox()
        self.search_line_edit = SearchLineEdit()
        self.search_button = widgets.IconButton('fa.search', color='#444', active_color='#3B6DBE')
        self.project_button = widgets.IconButton('fa.play', color='#444', active_color='#3B6DBE')
        self.update_button = widgets.IconButton('fa.refresh', color='#444', active_color='#3B6DBE')

        self.container.addWidget(self.versions_combo_box)
        self.container.addWidget(self.search_line_edit)
        self.container.addWidget(self.search_button)
        self.container.addWidget(self.project_button)
        self.container.addWidget(self.update_button)

        self.setLayout(self.container)
