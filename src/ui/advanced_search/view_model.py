from typing import List, Optional

from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.models.verse import Verse
from src.models.version import Version


class AdvancedSearchViewModel:
    verse_dao: VerseDAO
    version_dao: VersionDAO
    __versions: List[Version]

    def __init__(self) -> None:
        self.verse_dao = VerseDAO()
        self.version_dao = VersionDAO()

        self.__versions = self.version_dao.get_all()

    def get_version_options(self) -> List[str]:
        return ['Todas'] + [version.version for version in self.__versions]

    def search(self, search_text: str, version: Optional[str] = None) -> List[Verse]:
        if version == 'Todas':
            version = None
        return self.verse_dao.filter(
            {'q': search_text, 'version': version},
            limit=50
        )
