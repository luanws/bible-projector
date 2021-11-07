from typing import List, Optional

from src.dao.book_dao import BookDAO
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.models.verse import Verse
from src.models.version import Version


class AdvancedSearchViewModel:
    verse_dao: VerseDAO
    version_dao: VersionDAO
    book_dao: BookDAO
    __versions: List[Version]

    def __init__(self) -> None:
        self.verse_dao = VerseDAO()
        self.version_dao = VersionDAO()
        self.book_dao = BookDAO()

        self.__versions = self.version_dao.get_all()

    def get_all_version_options(self) -> List[str]:
        return ['Todas'] + [version.version for version in self.__versions]

    def get_all_book_options(self) -> List[str]:
        return ['Qualquer livro'] + [book.name for book in self.book_dao.get_all()]

    def search(self, search_text: str, book: str = None,  version: str = None) -> List[Verse]:
        if version == 'Todas':
            version = None
        if book == 'Qualquer livro':
            book = None
        return self.verse_dao.filter(
            {'q': search_text, 'version': version, 'book': book},
            limit=50
        )
