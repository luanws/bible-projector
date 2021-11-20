from typing import List, Optional

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QMainWindow,
                             QShortcut)
from sqlalchemy.orm.exc import NoResultFound
from src.error.invalid_reference import InvalidReferenceError
from src.models.verse import Verse
from src.ui.advanced_search import AdvancedSearchWindow
from src.ui.main.dialogs.about_dialog import AboutDialog
from src.ui.main.dialogs.installing_version_progress_dialog import \
    InstallingVersionProgressDialog
from src.ui.main.view_model import MainViewModel
from src.ui.main.widgets.history_widget import HistoryWidget
from src.ui.main.widgets.search_bar_widget import SearchBarWidget
from src.ui.main.window import Ui_MainWindow
from src.ui.projector import ProjectorWindow
from src.ui.settings import SettingsWindow
from src.utils.remote import Command
from src.utils.remote.remote_api import RemoteAPI
from src.widgets.chapter_widget import ChapterWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    __view_model: MainViewModel
    chapter_widget: ChapterWidget
    history_widget: HistoryWidget
    progress_dialog: Optional[InstallingVersionProgressDialog] = None

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = MainViewModel()
        self.settings_window = SettingsWindow()
        self.projector_window = ProjectorWindow()
        self.advanced_search_window = AdvancedSearchWindow(
            self.on_verse_clicked_advanced_search)
        self.about_dialog = AboutDialog()
        self.search_bar_widget = SearchBarWidget(
            versions=self.__view_model.versions,
            search_callable=self.search,
            project_callable=self.project,
            update_projector_text_callable=self.update_projector_text,
            on_change_current_version_callable=self.on_change_current_version,
        )
        self.chapter_widget = ChapterWidget(
            list_widget=self.chapter_list_widget,
            on_click=self.on_chapter_verse_click,
        )
        self.history_widget = HistoryWidget(
            list_widget=self.history_list_widget,
            on_reference_click=self.on_history_verse_click,
        )

        screen = QDesktopWidget().screenGeometry(2)
        self.projector_window.move(screen.left(), screen.top())

        self.header_container.addWidget(self.search_bar_widget)

        self.configure_events()
        self.configure_hot_keys()

    def configure_events(self):
        self.__view_model.on_change_current_verse(self.on_change_current_verse)

        self.action_export_history.triggered.connect(self.export_history)
        self.action_settings.triggered.connect(self.show_settings)
        self.action_about.triggered.connect(self.show_about)
        self.action_advanced_search.triggered.connect(
            self.show_advanced_search)
        self.action_quit.triggered.connect(self.close)
        self.action_install_version.triggered.connect(self.install_version)
        self.action_remote.triggered.connect(self.start_remote_api)

    def start_remote_api(self):
        remote_api = RemoteAPI()
        def on_search_by_reference(data):
            print(data)
            self.preview_text_edit.setText('teste123')
        remote_api.add_command_listener(Command.SEARCH_BY_REFERENCE, on_search_by_reference)
        remote_api.start()

    def on_verse_clicked_advanced_search(self, verse: Verse):
        self.__view_model.current_verse = verse

    def on_change_current_version(self, version: str):
        self.__view_model.current_version = version

    def on_change_current_verse(self, verse: Verse):
        self.preview_text_edit.setText(f"{verse.text} ({verse.reference})")
        self.update_projector_text()

    def on_history_verse_click(self, verse: Verse):
        self.__view_model.current_verse = verse
        self.__view_model.update_current_chapter(verse)
        self.update_chapter()
        self.select_current_verse_in_chapter()
        self.chapter_widget.scroll_to_verse(verse)

    def on_chapter_verse_click(self, verse: Verse):
        self.__view_model.current_verse = verse
        self.select_current_verse_in_chapter()

    def select_current_verse_in_chapter(self):
        self.chapter_widget.select_verse(self.__view_model.current_verse)

    def install_version(self):
        def on_update_progress(progress: int):
            if self.progress_dialog is None:
                self.progress_dialog = InstallingVersionProgressDialog(self)
                self.progress_dialog.setValue(0)
                self.progress_dialog.show()
            self.progress_dialog.setValue(progress*100)
            QCoreApplication.processEvents()
            if progress == 1:
                self.progress_dialog.hide()
                self.progress_dialog = None

        self.__view_model.install_version(on_update_progress)
        self.__view_model.update_versions()
        self.search_bar_widget.set_versions(self.__view_model.versions)

    def export_history(self):
        self.__view_model.export_history(self.history_widget.history)

    def show_about(self):
        self.about_dialog.show()

    def show_settings(self):
        self.settings_window.show()

    def show_advanced_search(self):
        self.advanced_search_window.show()

    def configure_hot_keys(self):
        hot_keys = [
            (Qt.Key_PageUp, self.next_verse, self),
            (Qt.Key_PageDown, self.previous_verse, self),
            (Qt.Key_F4, self.search_input_request_focus, self),
            (Qt.Key_F5, self.project, self),
            (Qt.Key_F6, self.update_projector_text, self),
            (Qt.Key_PageUp, self.next_verse, self.projector_window),
            (Qt.Key_PageDown, self.previous_verse, self.projector_window),
            (Qt.Key_Escape, self.close_projector, self),
        ]
        for hot_key, action, window in hot_keys:
            QShortcut(hot_key, window).activated.connect(action)

    def search_input_request_focus(self):
        self.search_bar_widget.search_input_request_focus()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.__view_model.application.quit()

    def previous_verse(self):
        try:
            verse = self.__view_model.previous_verse()
            self.select_current_verse_in_chapter()
            self.chapter_widget.scroll_to_verse(verse)
        except Exception:
            self.preview_text_edit.setText('Verso não encontrado')

    def next_verse(self):
        try:
            verse = self.__view_model.next_verse()
            self.select_current_verse_in_chapter()
            self.chapter_widget.scroll_to_verse(verse)
        except Exception:
            self.preview_text_edit.setText('Verso não encontrado')

    def set_occurrences(self, verses: List[Verse]):
        model = QtGui.QStandardItemModel()

        for verse in verses:
            item = QtGui.QStandardItem()
            item.setText(f"{verse.text} ({verse.reference})")
            model.appendRow(item)

        self.occurrences_list_view.setModel(model)
        self.occurrences_label.setText(f'Ocorrências: {len(verses)}')

    def update_projector_text(self):
        self.projector_window.text = self.preview_text_edit.toPlainText()

    def close_projector(self):
        self.projector_window.close()

    def project(self):
        screen = QApplication.screens()[-1]
        self.projector_window.show()
        self.projector_window.windowHandle().setScreen(screen)
        self.projector_window.showFullScreen()

    def update_chapter(self):
        self.chapter_widget.chapter = self.__view_model.current_chapter

    def search(self, search_text: str):
        try:
            verse = self.__view_model.search(search_text)
            self.history_widget.add_verse(verse)
            self.update_chapter()
            self.select_current_verse_in_chapter()
            self.chapter_widget.scroll_to_verse(verse)
            self.search_bar_widget.set_text(str(verse.reference))
        except InvalidReferenceError:
            self.preview_text_edit.setText('Referência bíblica inválida')
        except NoResultFound:
            self.preview_text_edit.setText('Texto não encontrado')
