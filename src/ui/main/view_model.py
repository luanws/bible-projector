from typing import Callable, List, Optional

from PyQt5.QtCore import QCoreApplication
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.error.invalid_reference import InvalidReferenceError
from src.models.chapter_reference import ChapterReference
from src.models.verse import Verse
from src.models.verse_reference import VerseReference
from src.models.version import Version


class MainViewModel:
    version_dao: VersionDAO
    verse_dao: VerseDAO
    current_version: Version
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

        self.versions = [v.version for v in self.version_dao.get_all()]
        self.current_version = self.versions[0]
        self.current_verse: Optional[Verse] = None
        self.current_chapter: Optional[List[Verse]] = None

    def on_change_current_verse(self, callable: Callable[[Verse], None]):
        self.__on_change_current_verse_callable = callable

    def search(self, search_text: str) -> Verse:
        if search_text != '':
            while search_text.__contains__('  '):
                search_text = search_text.replace('  ', ' ')
            version = self.current_version
            verse_reference = VerseReference.from_str(search_text, version)
            verse = self.verse_dao.get_by_verse_reference(verse_reference)
            self.current_verse = verse
            self.__update_current_chapter(verse)
            return verse
        raise InvalidReferenceError

    def __update_current_chapter(self, verse: Verse):
        self.current_chapter = self.verse_dao.get_by_chapter_reference(
            ChapterReference.from_verse_reference(verse.reference))
        return self.current_chapter

    def previous_verse(self) -> Verse:
        if self.current_verse is None:
            raise InvalidReferenceError('Nenhum verso selecionado')
        reference = self.current_verse.reference.previous()
        self.current_verse = self.verse_dao.get_by_verse_reference(reference)
        return self.current_verse

    def next_verse(self):
        reference = self.current_verse.reference.next()
        self.current_verse = self.verse_dao.get_by_verse_reference(reference)
        return self.current_verse
