import sqlite3

db = sqlite3.connect('test.db')

db.enable_load_extension(True)
db.load_extension('./res/sqlite-extensions/spellfix.so')

cursor = db.cursor()
cursor.execute("CREATE VIRTUAL TABLE texts USING fts4(description text)")
cursor.execute("CREATE VIRTUAL TABLE texts_terms USING fts4aux(texts)")
cursor.execute("CREATE VIRTUAL TABLE spellfix1data USING spellfix1")
# populate the table
cursor.execute("INSERT INTO texts VALUES ('All the Carmichael numbers')")
cursor.execute("INSERT INTO texts VALUES ('They are great')")
cursor.execute("INSERT INTO texts VALUES ('Here some other numbers')")
cursor.execute(
    "INSERT INTO spellfix1data(word) SELECT term FROM texts_terms WHERE col='*'")
db.commit()


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
