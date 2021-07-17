from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.decl_api import DeclarativeMeta


class Database:
    engine: Engine
    Base: DeclarativeMeta
    session: Session

    def __init__(self, url: str) -> None:
        self.engine = create_engine(url)
        self.Base = declarative_base()
        self.Base.metadata.create_all(self.engine)

        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()


db = Database('sqlite:///data/bible.db')
