from __future__ import annotations


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
