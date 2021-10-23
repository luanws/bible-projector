from typing import List

from src.database import db
from src.models import Book


class BookDAO:
    def get_all(self) -> List[Book]:
        return db.session.query(Book).all()
