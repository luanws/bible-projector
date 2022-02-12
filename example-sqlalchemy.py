import os
import sqlite3

from sqlalchemy.event import listen

from src.database import Database

os.remove('test.db')
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


db_sqlite3 = sqlite3.connect('test.db')
db_sqlite3.enable_load_extension(True)
db_sqlite3.load_extension('./res/sqlite-extensions/spellfix.so')
cursor = db_sqlite3.cursor()

def search(query):
    # Correcting each query term with spellfix table
    correctedquery = []
    for t in query.split():
        spellfix_query = "SELECT word FROM spellfix1data WHERE word MATCH ? and top=1"
        cursor.execute(spellfix_query, (t,))
        r = cursor.fetchone()
        # correct the word if any match in the spellfix table; if no match, keep the word spelled as it is (then the search will give no result!)
        correctedquery.append(r[0] if r is not None else t)

    correctedquery = ' '.join(correctedquery)

    # Now do the FTS
    fts_query = 'SELECT * FROM texts WHERE description MATCH ?'
    cursor.execute(fts_query, (correctedquery,))
    return {'result': cursor.fetchall(), 'correctedquery': correctedquery, 'query': query}


print(search('NUMBBERS carmickaeel'))
print(search('some HERE'))
print(search('some qsdhiuhsd'))
