from contextlib import suppress
from typing import Any, Dict, List

from sqlalchemy.orm.exc import NoResultFound
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
    'book_part': lambda q: func.lower(Book._name).like(f'%{q.lower()}%'),
    'chapter': lambda q: Verse.chapter_number == q,
    'verse': lambda q: Verse.verse_number == q,
    'q': lambda q: Verse.text.like(f'%{q}%'),
}


class VerseDAO:
    def get_by_verse_reference(self, verse_reference: VerseReference) -> Verse:
        filter_dict = {
            'book': verse_reference.book_name,
            'chapter': verse_reference.chapter_number,
            'verse': verse_reference.verse_number,
            'version': verse_reference.version,
        }
        verse_filter = query_filter_to_sql_filter_list(
            query_filter, filter_dict)
        with suppress(NoResultFound):
            return db.session.query(Verse)\
                .join(Version)\
                .join(Book)\
                .filter(*verse_filter).one()

        return self.get_by_verse_reference_with_book_name_part(verse_reference)

    def get_by_verse_reference_with_book_name_part(self, verse_reference: VerseReference) -> Verse:
        filter_dict = {
            'book_part': verse_reference.book_name,
            'chapter': verse_reference.chapter_number,
            'verse': verse_reference.verse_number,
            'version': verse_reference.version,
        }
        verse_filter = query_filter_to_sql_filter_list(
            query_filter, filter_dict)
        return db.session.query(Verse)\
            .join(Version)\
            .join(Book)\
            .filter(*verse_filter).first()

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
