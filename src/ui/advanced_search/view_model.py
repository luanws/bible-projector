from typing import List

from src.dao.book_dao import BookDAO
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.models.verse import Verse


class AdvancedSearchViewModel:
    verse_dao: VerseDAO
    version_dao: VersionDAO
    book_dao: BookDAO
    __version_names: List[str]
    __book_names: List[str]

    def __init__(self) -> None:
        self.verse_dao = VerseDAO()
        self.version_dao = VersionDAO()
        self.book_dao = BookDAO()

        self.__book_names = [b.name for b in self.book_dao.get_all()]
        self.update_versions()

    def update_versions(self) -> None:
        self.__version_names = [v.version for v in self.version_dao.get_all()]

    def get_all_version_options(self) -> List[str]:
        return ['Todas'] + self.__version_names

    def get_all_book_options(self) -> List[str]:
        return ['Qualquer livro'] + self.__book_names

    def search(self, search_text: str, book: str = None,  version: str = None) -> List[Verse]:
        if version not in self.__version_names:
            version = None
        if book not in self.__book_names:
            book = None
        return self.verse_dao.filter(
            {'q': search_text, 'version': version, 'book': book},
            limit=50
        )
