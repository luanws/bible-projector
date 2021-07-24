from contextlib import suppress
from typing import List, Optional

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QShortcut
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.error.invalid_reference import InvalidReferenceError
from src.models.chapter_reference import ChapterReference
from src.models.verse import Verse
from src.models.verse_reference import VerseReference
from src.ui.main.widgets.chapter_widget import ChapterWidget
from src.ui.main.window import Ui_MainWindow
from src.ui.projector import ProjectorWindow
from src.ui.settings import SettingsWindow

version_dao = VersionDAO()
verse_dao = VerseDAO()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.versions = [v.version for v in version_dao.get_all()]
        self.current_version = self.versions[0]
        self.__current_verse: Optional[Verse] = None
        self.current_chapter: Optional[List[Verse]] = None

        self.settings_window = SettingsWindow()
        self.projector_window = ProjectorWindow()
        screen = QDesktopWidget().screenGeometry(2)
        self.projector_window.move(screen.left(), screen.top())

        self.versions_combo_box.addItems(self.versions)
        self.search_button.clicked.connect(self.search)
        self.project_button.clicked.connect(self.project)
        self.update_button.clicked.connect(self.update_projector_text)
        self.settings_button.clicked.connect(self.show_settings)
        self.search_line_edit.returnPressed.connect(self.search)
        self.versions_combo_box.currentTextChanged.connect(self.update_version)

        self.configure_hot_keys()

    @property
    def current_verse(self):
        return self.__current_verse

    @current_verse.setter
    def current_verse(self, verse: Verse):
        self.__current_verse = verse
        self.preview_text_edit.setText(f"{verse.text} ({verse.reference})")
        self.update_projector_text()

    def show_settings(self):
        self.settings_window.show()

    def update_version(self):
        self.current_version = self.versions_combo_box.currentText()

    def configure_hot_keys(self):
        QShortcut(QtCore.Qt.Key_PageUp, self.projector_window).activated.connect(
            self.next_verse)
        QShortcut(QtCore.Qt.Key_PageDown, self.projector_window).activated.connect(
            self.previous_verse)
        QShortcut(QtCore.Qt.Key_PageUp, self).activated.connect(
            self.next_verse)
        QShortcut(QtCore.Qt.Key_PageDown, self).activated.connect(
            self.previous_verse)
        QShortcut(QtCore.Qt.Key_F4, self).activated.connect(
            self.search_input_request_focus)
        QShortcut(QtCore.Qt.Key_F5, self).activated.connect(
            self.project)
        QShortcut(QtCore.Qt.Key_Escape, self).activated.connect(
            self.close_projector)
        QShortcut(QtCore.Qt.Key_F6, self).activated.connect(
            self.update_projector_text)

    def search_input_request_focus(self):
        self.search_line_edit.setFocus(True)
        self.search_line_edit.selectAll()

    def previous_verse(self):
        try:
            reference = self.current_verse.reference.previous()
            self.current_verse = verse_dao.get_by_verse_reference(reference)
        except Exception:
            self.preview_text_edit.setText('Verso não encontrado')

    def next_verse(self):
        try:
            reference = self.current_verse.reference.next()
            self.current_verse = verse_dao.get_by_verse_reference(reference)
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
        self.projector_window.showFullScreen()

    def update_chapter(self):
        current_chapter = verse_dao.get_by_chapter_reference(
            ChapterReference.from_verse_reference(self.current_verse.reference))
        self.current_chapter = current_chapter
        for verse in current_chapter:
            chapter_widget = ChapterWidget(verse=verse)
            list_widget_item = QtWidgets.QListWidgetItem(
                self.chapter_list_widget)
            list_widget_item.setSizeHint(chapter_widget.sizeHint())
            self.chapter_list_widget.addItem(list_widget_item)
            self.chapter_list_widget.setItemWidget(
                list_widget_item, chapter_widget)

    def search(self):
        search_text = self.search_line_edit.text()
        if search_text != '':
            try:
                version = self.current_version
                verse_reference = VerseReference.from_str(search_text, version)
                verse = verse_dao.get_by_verse_reference(verse_reference)
                self.current_verse = verse
                self.update_chapter()
            except InvalidReferenceError:
                with suppress(IndexError):
                    verses = verse_dao.filter({
                        'q': search_text,
                        'version': self.current_version,
                    }, limit=100)
                    self.current_verse = verses[0]
                    self.set_occurrences(verses)
