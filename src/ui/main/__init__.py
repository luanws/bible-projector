from typing import List, Optional

from PyQt5 import QtGui, QtWidgets
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
from src.ui.main.widgets.chapter_widget import ChapterVerseWidget
from src.ui.main.widgets.history_widget import HistoryWidget
from src.ui.main.widgets.search_bar_widget import SearchBarWidget
from src.ui.main.window import Ui_MainWindow
from src.ui.projector import ProjectorWindow
from src.ui.settings import SettingsWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __view_model: MainViewModel
    chapter_verse_widgets: Optional[List[ChapterVerseWidget]]

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = MainViewModel()
        self.settings_window = SettingsWindow()
        self.projector_window = ProjectorWindow()
        self.advanced_search_window = AdvancedSearchWindow()
        self.about_dialog = AboutDialog()
        self.search_bar_widget = SearchBarWidget(
            versions=self.__view_model.versions,
            search_callable=self.search,
            project_callable=self.project,
            update_projector_text_callable=self.update_projector_text,
            on_change_current_verse_callable=self.on_change_current_version,
        )

        screen = QDesktopWidget().screenGeometry(2)
        self.projector_window.move(screen.left(), screen.top())

        self.header_container.addWidget(self.search_bar_widget)

        self.configure_events()
        self.configure_hot_keys()

    @property
    def current_chapter_verse_widget(self):
        return self.chapter_verse_widgets[self.__view_model.current_verse.verse_number - 1]

    def configure_events(self):
        self.__view_model.on_change_current_verse(self.on_change_current_verse)

        self.action_export_history.triggered.connect(
            self.__view_model.export_history)
        self.action_settings.triggered.connect(self.show_settings)
        self.action_about.triggered.connect(self.show_about)
        self.action_advanced_search.triggered.connect(
            self.show_advanced_search)
        self.action_quit.triggered.connect(self.close)
        self.action_install_version.triggered.connect(self.install_version)

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
        self.chapter_list_widget.scrollToItem(
            self.current_chapter_verse_widget.list_widget_item)

    def on_history_verse_remove(self, verse: Verse):
        self.__view_model.remove_from_history(verse)
        self.update_history()

    def on_chapter_verse_click(self, verse: Verse):
        self.__view_model.current_verse = verse
        self.select_current_verse_in_chapter()

    def select_current_verse_in_chapter(self):
        if self.chapter_verse_widgets is not None:
            for chapter_verse_widget in self.chapter_verse_widgets:
                chapter_verse_widget.unselect()
            chapter_verse_widget = self.current_chapter_verse_widget
            chapter_verse_widget.select()

    def install_version(self):
        progress_dialog = InstallingVersionProgressDialog(self)

        def on_update_progress(progress: int):
            QCoreApplication.processEvents()
            progress_dialog.setValue(progress*100)
            if progress == 0:
                progress_dialog.show()
            elif progress == 1:
                progress_dialog.destroy()

        self.__view_model.install_version(on_update_progress)
        self.__view_model.update_versions()
        self.search_bar_widget.set_versions(self.__view_model.versions)

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

    def scroll_to_chapter_verse_widget_by_index(self, index: int):
        if self.chapter_verse_widgets is not None:
            chapter_verse_widget = self.chapter_verse_widgets[index]
            if chapter_verse_widget.visibleRegion().isEmpty():
                self.chapter_list_widget.scrollToItem(
                    self.current_chapter_verse_widget.list_widget_item)
            else:
                self.chapter_list_widget.scrollToItem(
                    chapter_verse_widget.list_widget_item)

    def previous_verse(self):
        try:
            index = self.__view_model.previous_verse()
            self.select_current_verse_in_chapter()
            self.scroll_to_chapter_verse_widget_by_index(index)
        except Exception:
            self.preview_text_edit.setText('Verso não encontrado')

    def next_verse(self):
        try:
            index = self.__view_model.next_verse()
            self.select_current_verse_in_chapter()
            self.scroll_to_chapter_verse_widget_by_index(index)
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
        self.chapter_list_widget.clear()
        chapter_verse_widgets = []
        for verse in self.__view_model.current_chapter:
            list_widget_item = QtWidgets.QListWidgetItem(
                self.chapter_list_widget)
            chapter_verse_widget = ChapterVerseWidget(
                verse=verse,
                list_widget_item=list_widget_item,
                on_click=self.on_chapter_verse_click,
            )
            list_widget_item.setSizeHint(chapter_verse_widget.sizeHint())
            self.chapter_list_widget.addItem(list_widget_item)
            self.chapter_list_widget.setItemWidget(
                list_widget_item, chapter_verse_widget)
            chapter_verse_widgets.append(chapter_verse_widget)
        self.chapter_verse_widgets = chapter_verse_widgets

    def update_history(self):
        self.history_list_widget.clear()
        for verse in self.__view_model.history_list:
            list_widget_item = QtWidgets.QListWidgetItem(
                self.history_list_widget)
            history_widget = HistoryWidget(
                verse=verse,
                list_widget_item=list_widget_item,
                on_reference_click=self.on_history_verse_click,
                on_remove_click=self.on_history_verse_remove,
            )
            list_widget_item.setSizeHint(history_widget.sizeHint())
            self.history_list_widget.addItem(list_widget_item)
            self.history_list_widget.setItemWidget(
                list_widget_item, history_widget)

    def search(self, search_text: str):
        try:
            verse = self.__view_model.search(search_text)
            self.update_history()
            self.update_chapter()
            self.select_current_verse_in_chapter()
            self.chapter_list_widget.scrollToItem(
                self.current_chapter_verse_widget.list_widget_item)
            self.search_bar_widget.set_text(str(verse.reference))
        except InvalidReferenceError:
            self.preview_text_edit.setText('Referência bíblica inválida')
        except NoResultFound:
            self.preview_text_edit.setText('Texto não encontrado')
