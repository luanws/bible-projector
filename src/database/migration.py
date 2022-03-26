from abc import ABC, abstractstaticmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.database import Database


class Migration(ABC):
    @abstractstaticmethod
    def up(self, db: 'Database'):
        pass

    @abstractstaticmethod
    def down(self, db: 'Database'):
        pass
