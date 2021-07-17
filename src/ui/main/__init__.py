from contextlib import suppress
from typing import List, Optional

import PyQt5.QtGui as QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.models.chapter_reference import ChapterReference
from src.models.verse import Verse
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

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key == QtCore.Qt.Key_F4:
            self.pesquisaLineEdit.setFocus(True)
            self.pesquisaLineEdit.selectAll()
        elif key == QtCore.Qt.Key_F5:
            self.project()
        elif key == QtCore.Qt.Key_Escape:
            self.close_projector()
        elif key == QtCore.Qt.Key_F6:
            self.update_projector_text()
        elif key == QtCore.Qt.Key_PageUp:
            self.next_verse()
        elif key == QtCore.Qt.Key_PageDown:
            self.previous_verse()

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
            with suppress(IndexError):
                verses = verse_dao.search(
                    search_text,
                    self.current_version,
                    limit=100
                )
                self.current_verse = verses[0]
                self.set_occurrences(verses)
                self.update_chapter()
