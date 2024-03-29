from typing import Callable, Optional

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from src.models.verse import Verse
from src.utils import styles
from src.utils.settings.theme_settings import ThemeSettings

from .container import Container
from .reference_button import ReferenceButton
from .remove_button import RemoveButton


class HistoryItemWidget(QtWidgets.QWidget):
    verse: Verse
    list_widget_item: QtWidgets.QListWidgetItem
    reference_clicked = pyqtSignal(Verse)
    remove_clicked = pyqtSignal(Verse)
    theme_settings: ThemeSettings

    def __init__(
        self, parent=None, *,
        verse: Verse,
        list_widget_item: QtWidgets.QListWidgetItem,
    ):
        super(HistoryItemWidget, self).__init__(parent)

        self.verse = verse
        self.list_widget_item = list_widget_item

        self.theme_settings = ThemeSettings()

        self.container = Container()
        self.reference_button = ReferenceButton()
        self.remove_button = RemoveButton()

        self.reference_button.setText(str(verse.reference))

        self.container.addWidget(self.reference_button)
        self.container.addWidget(self.remove_button)
        self.setLayout(self.container)

        self.apply_styles()
        self.theme_settings.add_settings_listener(self.apply_styles)

        self.configure_events()

    def apply_styles(self):
        try:
            self.setStyleSheet(styles.get_qss_stylesheet(
                'src/ui/main/widgets/history_widget/history_item_widget/styles.qss'))
        except RuntimeError:
            self.theme_settings.remove_settings_listener()

    def configure_events(self):
        self.reference_button.clicked.connect(self.on_reference_button_click)
        self.remove_button.clicked.connect(self.on_remove_button_click)

    def on_remove_button_click(self):
        self.remove_clicked.emit(self.verse)

    def on_reference_button_click(self):
        self.reference_clicked.emit(self.verse)
