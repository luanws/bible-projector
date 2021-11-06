from contextlib import suppress
from typing import Callable, List, Optional

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.error.invalid_reference import InvalidReferenceError
from src.models.chapter_reference import ChapterReference
from src.models.verse import Verse
from src.models.verse_reference import VerseReference
from src.utils.modules.versions import select_file_and_install_version


class MainViewModel:
    version_dao: VersionDAO
    verse_dao: VerseDAO
    current_version: str
    __current_verse: Optional[Verse]
    current_chapter: Optional[List[Verse]]
    __on_change_current_verse_callable: Optional[Callable[[
        Verse], None]] = None

    @property
    def current_verse(self) -> Optional[Verse]:
        return self.__current_verse

    @current_verse.setter
    def current_verse(self, verse: Verse):
        self.__current_verse = verse
        if self.__on_change_current_verse_callable is not None:
            self.__on_change_current_verse_callable(verse)

    def __init__(self):
        self.version_dao = VersionDAO()
        self.verse_dao = VerseDAO()

        self.application: QCoreApplication = QCoreApplication.instance()

        self.update_versions()
        self.current_version = self.versions[0]
        self.__current_verse: Optional[Verse] = None
        self.current_chapter: Optional[List[Verse]] = None

    def update_versions(self):
        self.versions = [v.version for v in self.version_dao.get_all()]

    def on_change_current_verse(self, callable: Callable[[Verse], None]):
        self.__on_change_current_verse_callable = callable

    def export_history(self, history: List[Verse]):
        with suppress(FileNotFoundError):
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(
                self.application.activeWindow(),
                "Salvar como",
                "Histórico",
                "Documentos de texto (*.txt)"
            )
            with open(filename, 'w') as file:
                for verse in history:
                    file.write(str(verse.reference) + '\n')

    def search(self, search_text: str) -> Verse:
        if search_text != '':
            while search_text.__contains__('  '):
                search_text = search_text.replace('  ', ' ')
            version = self.current_version
            verse_reference = VerseReference.from_str(search_text, version)
            verse = self.verse_dao.get_by_verse_reference(verse_reference)
            self.current_verse = verse
            self.update_current_chapter(verse)
            return verse
        raise InvalidReferenceError

    def update_current_chapter(self, verse: Verse):
        self.current_chapter = self.verse_dao.get_by_chapter_reference(
            ChapterReference.from_verse_reference(verse.reference))
        return self.current_chapter

    def previous_verse(self) -> Verse:
        if self.current_verse is None or self.current_chapter is None:
            raise InvalidReferenceError('Nenhum verso selecionado')
        index = self.current_verse.verse_number - 2
        if index < 0:
            raise InvalidReferenceError('Não há versículo anterior')
        self.current_verse = self.current_chapter[index]
        return self.current_verse

    def next_verse(self) -> Verse:
        if self.current_verse is None or self.current_chapter is None:
            raise InvalidReferenceError('Nenhum verso selecionado')
        index = self.current_verse.verse_number
        if index >= len(self.current_chapter):
            raise InvalidReferenceError('Não há versículo posterior')
        self.current_verse = self.current_chapter[index]
        return self.current_verse

    def install_version(self, on_update_progress: Optional[Callable] = None):
        select_file_and_install_version(on_update_progress)
