import json
from typing import Dict, List

from src.dao.book_dao import BookDAO
from src.dao.verse_dao import VerseDAO
from src.models.book import Book
from src.models.verse import Verse


def get_bible_shape(books: List[Book], verses: List[Verse]) -> Dict[str, Dict[str, int]]:
    bible_shape: Dict[str, Dict[str, int]] = {}
    for book in books:
        bible_shape[str(book.id)] = {}
        verses_of_book = [v for v in verses if v.book_id == book.id]
        first_verses = [v for v in verses_of_book if v.verse_number == 1]
        number_of_chapters = len(first_verses)
        for chapter in range(1, number_of_chapters + 1):
            verses_of_chapter = [
                v for v in verses_of_book if v.chapter_number == chapter]
            bible_shape[str(book.id)][str(chapter)] = len(verses_of_chapter)
    return bible_shape


def generate_bible_shape():
    book_dao = BookDAO()
    verse_dao = VerseDAO()
    books = book_dao.get_all()
    verses = verse_dao.filter({'version': 'ARA'})
    bible_shape = get_bible_shape(books, verses)
    bible_shape_str = json.dumps(bible_shape)
    with open('data/bible_shape.json', 'w', encoding='utf8') as f:
        f.write(bible_shape_str)


if __name__ == '__main__':
    generate_bible_shape()
