from typing import List

from src.database import db
from src.models import Version


class VersionDAO:
    def get_all(self) -> List[Version]:
        return db.session.query(Version).all()

    def add(self, version: Version):
        db.session.add(version)
        db.session.commit()

    def delete(self, id: int):
        db.session.query(Version).filter(Version.id == id).delete()
        db.session.commit()

    def delete_by_version_name(self, name: str):
        db.session.query(Version).filter(Version.version == name).delete()
        db.session.commit()
