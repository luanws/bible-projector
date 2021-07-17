from __future__ import annotations

from src.models.verse_reference import VerseReference


class ChapterReference:
    book_name: str
    chapter_number: int
    version: str

    def __init__(self, book_name: str, chapter_number: int, version: str) -> None:
        self.book_name = book_name
        self.chapter_number = chapter_number
        self.version = version

    @staticmethod
    def from_verse_reference(verse_reference: VerseReference) -> ChapterReference:
        return ChapterReference(
            book_name=verse_reference.book_name,
            chapter_number=verse_reference.chapter_number,
            version=verse_reference.version
        )
