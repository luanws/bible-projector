from src.error.invalid_reference import InvalidReferenceError
from typing import List, Optional
from src.models.verse import Verse
from src.models.version import Version

from src.models.verse_reference import VerseReference
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO


class MainViewModel:
    version_dao: VersionDAO
    verse_dao: VerseDAO
    current_version: Version
    current_verse: Optional[Verse]
    current_chapter: Optional[List[Verse]]

    def __init__(self):
        self.version_dao = VersionDAO()
        self.verse_dao = VerseDAO()

        self.versions = [v.version for v in self.version_dao.get_all()]
        self.current_version = self.versions[0]
        self.current_verse: Optional[Verse] = None
        self.current_chapter: Optional[List[Verse]] = None

    def search(self, search_text: str) -> Verse:
        if search_text != '':
            while search_text.__contains__('  '):
                search_text = search_text.replace('  ', ' ')
            version = self.current_version
            verse_reference = VerseReference.from_str(search_text, version)
            verse = self.verse_dao.get_by_verse_reference(verse_reference)
            self.current_verse = verse
            return verse
        raise InvalidReferenceError
