from typing import List
from PyQt5 import QtWidgets
from src.dao.book_dao import BookDAO

from src.models.verse import Verse
from src.models.book import Book


def get_version_file_path() -> str:
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        None,
        "Instalar versão",
        "",
        "Versões da bíblia (*.ont)"
    )
    return file_path


def bible_text_to_verses(bible_text: str, books: List[Book]) -> List[Verse]:
    verse_str_list = bible_text.split('\n')


def install_version():
    file_path = get_version_file_path()
    with open(file_path, encoding='utf8') as f:
        bible_text = f.read()
    book_dao = BookDAO()
    books = book_dao.get_all()
    verses = bible_text_to_verses(bible_text, books)
    print([b.name for b in books])
