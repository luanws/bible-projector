from contextlib import suppress
from typing import Callable, List

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from src import widgets
from src.models.version import Version
from src.utils import styles
from src.utils.settings.theme_settings import ThemeSettings

from .container import Container
from .search_line_edit import SearchLineEdit
from .versions_combo_box import VersionsComboBox


class SearchBarWidget(QtWidgets.QWidget):
    theme_settings: ThemeSettings
    versions: List[Version]
    update_clicked = pyqtSignal()
    change_version = pyqtSignal(str)

    def __init__(
        self, parent=None, *,
        versions: List[Version],
        search_callable: Callable[[str], None],
        project_callable: Callable[[], None],
    ) -> None:
        super(SearchBarWidget, self).__init__(parent)

        self.versions = versions
        self.search_callable = search_callable
        self.project_callable = project_callable

        self.theme_settings = ThemeSettings()
        self.container = Container()

        self.render()
        self.theme_settings.add_settings_listener(self.render)

        self.setLayout(self.container)

    def render(self):
        with suppress(AttributeError):
            self.container.removeWidget(self.versions_combo_box)
            self.container.removeWidget(self.search_line_edit)
            self.container.removeWidget(self.search_button)
            self.container.removeWidget(self.project_button)
            self.container.removeWidget(self.update_button)

        self.versions_combo_box = VersionsComboBox()
        self.search_line_edit = SearchLineEdit(search_callable=self.search)

        color = styles.qss_vars['@colorIcon']
        active_color = styles.qss_vars['@colorActiveIcon']

        self.search_button = widgets.IconButton(
            'fa.search', color=color, active_color=active_color)
        self.project_button = widgets.IconButton(
            'fa.play', color=color, active_color=active_color)
        self.update_button = widgets.IconButton(
            'fa.refresh', color=color, active_color=active_color)

        self.versions_combo_box.addItems(self.versions)

        self.container.addWidget(self.versions_combo_box)
        self.container.addWidget(self.search_line_edit)
        self.container.addWidget(self.search_button)
        self.container.addWidget(self.project_button)
        self.container.addWidget(self.update_button)

        self.setStyleSheet(styles.get_qss_stylesheet(
            'src/ui/main/widgets/search_bar_widget/styles.qss'))

        self.configure_events()

    def set_versions(self, versions: List[Version]) -> None:
        self.versions = versions
        self.versions_combo_box.clear()
        self.versions_combo_box.addItems(versions)

    def configure_events(self):
        self.search_button.clicked.connect(self.search)
        self.project_button.clicked.connect(self.project_callable)
        self.update_button.clicked.connect(self.update_clicked.emit)
        self.versions_combo_box.change_version.connect(
            self.change_version.emit)

    def search(self):
        self.search_callable(self.search_line_edit.text())

    def search_input_request_focus(self) -> None:
        self.search_line_edit.request_focus()

    def set_text(self, text: str) -> None:
        self.search_line_edit.setText(text)
