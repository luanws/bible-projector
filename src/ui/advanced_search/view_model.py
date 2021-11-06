from typing import List

from src.dao.verse_dao import VerseDAO
from src.models.verse import Verse


class AdvancedSearchViewModel:
    verse_dao: VerseDAO

    def __init__(self) -> None:
        self.verse_dao = VerseDAO()

    def search(self, search_text: str) -> List[Verse]:
        return self.verse_dao.filter({'q': search_text})
