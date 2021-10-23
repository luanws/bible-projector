from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from src.database import db


class Version(db.Base):
    __tablename__ = 'versions'

    id = Column(Integer, primary_key=True)
    version = Column(String, nullable=False)

    def __init__(self, *, id: int = None, version: str) -> None:
        self.id = id
        self.version = version
