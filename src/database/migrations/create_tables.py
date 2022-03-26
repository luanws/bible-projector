from typing import TYPE_CHECKING

from src.database.migration import Migration

if TYPE_CHECKING:
    from src.database import Database


class CreateTablesMigration(Migration):
    @staticmethod
    def up(db: 'Database'):
        db.session.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                testament TEXT NOT NULL
            )
        """)

        db.session.execute("""
            CREATE TABLE IF NOT EXISTS chapters (
                id INTEGER PRIMARY KEY,
                book_id INTEGER NOT NULL,
                number INTEGER NOT NULL,
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        """)

        db.session.execute("""
            CREATE TABLE IF NOT EXISTS verses (
                id INTEGER PRIMARY KEY,
                chapter_id INTEGER NOT NULL,
                number INTEGER NOT NULL,
                FOREIGN KEY (chapter_id) REFERENCES chapters(id)
            )
        """)

        db.session.execute("""
            CREATE TABLE IF NOT EXISTS verses_text (
                id INTEGER PRIMARY KEY,
                verse_id INTEGER NOT NULL,
                text TEXT NOT NULL,
                FOREIGN KEY (verse_id) REFERENCES verses(id)
            )
        """)

    @staticmethod
    def down(db: 'Database'):
        db.session.execute("DROP TABLE IF EXISTS verses_text")
        db.session.execute("DROP TABLE IF EXISTS verses")
        db.session.execute("DROP TABLE IF EXISTS chapters")
        db.session.execute("DROP TABLE IF EXISTS books")
