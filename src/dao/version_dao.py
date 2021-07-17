from typing import List

from src.database import db
from src.models import Version


class VersionDAO:
    def get_all(self) -> List[Version]:
        texts = db.session.query(Version).all()
        return texts
