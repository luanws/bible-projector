from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from src.database import db


class Book(db.Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    _name = Column(String, nullable=False)
    _initials = Column(String, nullable=False)
