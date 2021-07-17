import re
from contextlib import suppress
from typing import Any, Dict, List

from sqlalchemy.sql.expression import func, or_
from src.database import db
from src.models import Book, Verse, Version
from src.models.chapter_reference import ChapterReference
from src.models.verse_reference import VerseReference
from src.models.version import Version
from src.utils.query_filter import QueryFilter, query_filter_to_sql_filter_list

query_filter: QueryFilter = {
    'version': lambda q: Version.version == q if q else True,
    'book': lambda q: or_(
        func.lower(Book.name) == func.lower(q),
        func.lower(Book._name) == func.lower(q),
        func.lower(Book._initials) == func.lower(q),
    ),
    'chapter': lambda q: Verse.chapter_number == q,
    'verse': lambda q: Verse.verse_number == q,
    'q': lambda q: Verse.text.like(f'%{q}%'),
}


class VerseDAO:
    def search(self, search_text: str, version: str = None, limit: int = None) -> List[Verse]:
        with suppress(AttributeError):
            regex = r'^(.+)\s+(\d+)[\s|:]+(\d+)$'
            book, chapter_number, verse_number = re.search(
                regex, search_text).groups()
            filter_dict = {
                'book': book,
                'chapter': chapter_number,
                'verse': verse_number
            }
            if version is not None:
                filter_dict['version'] = version
            return self.filter(filter_dict, limit=limit)

        filter_dict = {'q': search_text}
        if version is not None:
            filter_dict['version'] = version
        return self.filter(filter_dict, limit=limit)

    def get_by_verse_reference(self, verse_reference: VerseReference) -> Verse:
        verse_filter = (
            Book.name == verse_reference.book_name,
            Verse.chapter_number == verse_reference.chapter_number,
            Verse.verse_number == verse_reference.verse_number,
            Version.version == verse_reference.version
        )
        return db.session.query(Verse)\
            .join(Version)\
            .join(Book)\
            .filter(*verse_filter).one()

    def get_by_chapter_reference(self, chapter_reference: ChapterReference) -> List[Verse]:
        verse_filter = (
            Book.name == chapter_reference.book_name,
            Verse.chapter_number == chapter_reference.chapter_number,
            Version.version == chapter_reference.version
        )
        return db.session.query(Verse)\
            .join(Version)\
            .join(Book)\
            .filter(*verse_filter).all()

    def filter(self, filter_dict: Dict[str, Any], limit: int = None) -> List[Verse]:
        verse_filter = query_filter_to_sql_filter_list(
            query_filter, filter_dict)
        query = db.session.query(Verse)\
            .join(Version)\
            .join(Book)\
            .filter(*verse_filter)
        return query.all() if limit is None else query[:limit]
