from typing import Callable, List

from PyQt5 import QtWidgets
from src import widgets
from src.models.version import Version
from src.utils import styles

from .container import Container
from .search_line_edit import SearchLineEdit
from .versions_combo_box import VersionsComboBox


class SearchBarWidget(QtWidgets.QWidget):
    def __init__(
        self, parent=None, *,
        versions: List[Version],
        search_callable: Callable[[str], None],
        project_callable: Callable[[], None],
        update_projector_text_callable: Callable[[], None],
        on_change_current_version_callable: Callable[[str], None],
    ) -> None:
        super(SearchBarWidget, self).__init__(parent)

        self.versions = versions
        self.search_callable = search_callable
        self.project_callable = project_callable
        self.update_projector_text_callable = update_projector_text_callable
        self.on_change_current_version_callable = on_change_current_version_callable

        self.container = Container()
        self.versions_combo_box = VersionsComboBox(
            on_change_current_version_callable=self.on_change_current_version_callable,
        )
        self.search_line_edit = SearchLineEdit(search_callable=self.search)
        color = styles.qss_vars['@colorIcon']
        active_color = styles.qss_vars['@colorActiveIcon']
        self.search_button = widgets.IconButton(
            'fa.search', color=color, active_color=active_color)
        self.project_button = widgets.IconButton(
            'fa.play', color=color, active_color=active_color)
        self.update_button = widgets.IconButton(
            'fa.refresh', color=color, active_color=active_color)

        self.versions_combo_box.addItems(versions)

        self.container.addWidget(self.versions_combo_box)
        self.container.addWidget(self.search_line_edit)
        self.container.addWidget(self.search_button)
        self.container.addWidget(self.project_button)
        self.container.addWidget(self.update_button)

        self.configure_events()
        self.setLayout(self.container)

        self.setStyleSheet(styles.get_qss_stylesheet('src/ui/main/widgets/search_bar_widget/styles.qss'))

    def set_versions(self, versions: List[Version]) -> None:
        self.versions = versions
        self.versions_combo_box.clear()
        self.versions_combo_box.addItems(versions)

    def configure_events(self):
        self.search_button.clicked.connect(self.search)
        self.project_button.clicked.connect(self.project_callable)
        self.update_button.clicked.connect(self.update_projector_text_callable)

    def search(self):
        self.search_callable(self.search_line_edit.text())

    def search_input_request_focus(self) -> None:
        self.search_line_edit.request_focus()

    def set_text(self, text: str) -> None:
        self.search_line_edit.setText(text)
