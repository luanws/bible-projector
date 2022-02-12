import os
import sqlite3
from contextlib import suppress

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.event import listen
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm.session import Session

with suppress(Exception):
    os.remove('test.db')


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


db = Database('sqlite:///test.db')


def load_extension(connection: sqlite3.Connection, _):
    connection.enable_load_extension(True)
    connection.load_extension('./res/sqlite-extensions/spellfix.so')


listen(db.engine, 'connect', load_extension)

db.session.execute("CREATE VIRTUAL TABLE texts USING fts4(description text)")
db.session.execute("CREATE VIRTUAL TABLE texts_terms USING fts4aux(texts)")
db.session.execute("CREATE VIRTUAL TABLE spellfix1data USING spellfix1")
db.session.execute("INSERT INTO texts VALUES ('All the Carmichael numbers')")
db.session.execute("INSERT INTO texts VALUES ('They are great')")
db.session.execute("INSERT INTO texts VALUES ('Here some other numbers')")
db.session.execute(
    "INSERT INTO spellfix1data(word) SELECT term FROM texts_terms WHERE col='*'")
db.session.commit()


def search(search_text: str):
    corrected_words: list[str] = []
    for word in search_text.split():
        spellfix_query = f"SELECT word FROM spellfix1data WHERE word MATCH '{word}' and top=1"
        row = db.session.execute(spellfix_query).fetchone()
        corrected_words.append(word if row is None else row[0])

    corrected_search_text: str = ' '.join(corrected_words)
    print(search_text, '->', corrected_search_text)

    fts_query = f"SELECT * FROM texts WHERE description MATCH '{corrected_search_text}'"
    cursor = db.session.execute(fts_query)
    return {'result': cursor.fetchall(), 'correctedquery': corrected_search_text, 'query': search_text}


print(search('NUMBBERS carmickaeel'))
print(search('some HERE'))
print(search('some qsdhiuhsd'))
