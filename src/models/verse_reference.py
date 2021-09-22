from __future__ import annotations

import re

from src.error.invalid_reference import InvalidReferenceError


class VerseReference:
    book_name: str
    chapter_number: int
    verse_number: int
    version: str

    def __init__(self, book_name: str, chapter_number: int, verse_number: int, version: str) -> None:
        self.book_name = book_name
        self.chapter_number = chapter_number
        self.verse_number = verse_number
        self.version = version

    def __str__(self) -> str:
        return f'{self.book_name} {self.chapter_number}:{self.verse_number}'

    @staticmethod
    def from_str(reference_str: str, version: str) -> VerseReference:
        try:
            regex = r'^(.+)\s+(\d+)[\s|:]+(\d+)$'
            search_result = re.search(regex, reference_str)
            if search_result is None:
                raise InvalidReferenceError()
            book, chapter_number, verse_number = search_result.groups()
            return VerseReference(
                book_name=book,
                chapter_number=int(chapter_number),
                verse_number=int(verse_number),
                version=version
            )
        except AttributeError:
            raise InvalidReferenceError()

    def previous(self) -> VerseReference:
        return VerseReference(
            book_name=self.book_name,
            chapter_number=self.chapter_number,
            verse_number=self.verse_number-1,
            version=self.version,
        )

    def next(self) -> VerseReference:
        return VerseReference(
            book_name=self.book_name,
            chapter_number=self.chapter_number,
            verse_number=self.verse_number+1,
            version=self.version,
        )
