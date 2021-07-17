from contextlib import suppress
from typing import List, Optional

import PyQt5.QtGui as QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QShortcut
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.error.invalid_reference import InvalidReferenceError
from src.models.chapter_reference import ChapterReference
from src.models.verse import Verse
from src.models.verse_reference import VerseReference
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

        self.versoesComboBox.addItems(self.versions)
        self.pesquisarButton.clicked.connect(self.search)
        self.projetarButton.clicked.connect(self.project)
        self.atualizarButton.clicked.connect(self.update_projector_text)
        self.configuracoesButton.clicked.connect(self.show_settings)
        self.pesquisaLineEdit.returnPressed.connect(self.search)
        self.versoesComboBox.currentTextChanged.connect(self.update_version)

        self.configure_hot_keys()

    @property
    def current_verse(self):
        return self.__current_verse

    @current_verse.setter
    def current_verse(self, verse: Verse):
        self.__current_verse = verse
        self.previewTextEdit.setText(f"{verse.text} ({verse.reference})")
        self.update_projector_text()

    def show_settings(self):
        self.settings_window.show()

    def update_version(self):
        self.current_version = self.versoesComboBox.currentText()

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
        self.pesquisaLineEdit.setFocus(True)
        self.pesquisaLineEdit.selectAll()

    def previous_verse(self):
        try:
            reference = self.current_verse.reference.previous()
            self.current_verse = verse_dao.get_by_verse_reference(reference)
        except Exception:
            self.previewTextEdit.setText('Verso não encontrado')

    def next_verse(self):
        try:
            reference = self.current_verse.reference.next()
            self.current_verse = verse_dao.get_by_verse_reference(reference)
        except Exception:
            self.previewTextEdit.setText('Verso não encontrado')

    def set_occurrences(self, verses: List[Verse]):
        model = QtGui.QStandardItemModel()

        for verse in verses:
            item = QtGui.QStandardItem()
            item.setText(f"{verse.text} ({verse.reference})")
            model.appendRow(item)

        self.occurrencesListView.setModel(model)
        self.ocorrenciasLabel.setText(f'Ocorrências: {len(verses)}')

    def update_projector_text(self):
        self.projector_window.text = self.previewTextEdit.toPlainText()

    def close_projector(self):
        self.projector_window.close()

    def project(self):
        self.projector_window.showFullScreen()

    def update_chapter(self):
        current_chapter = verse_dao.get_by_chapter_reference(
            ChapterReference.from_verse_reference(self.current_verse.reference))
        self.current_chapter = current_chapter
        model = QtGui.QStandardItemModel()
        for verse in current_chapter:
            item = QtGui.QStandardItem()
            item.setText(f"{verse.text} ({verse.reference})")
            model.appendRow(item)
        self.chapterListView.setModel(model)

    def search(self):
        search_text = self.pesquisaLineEdit.text()
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
