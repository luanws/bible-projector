import json
import os
import re
from typing import Callable, Dict, Optional

from PyQt5 import QtWidgets
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.models.version import Version

from .parsers import content_to_verses


def get_bible_shape() -> Dict[str, Dict[str, int]]:
    with open('data/bible_shape.json') as f:
        bible_shape = json.load(f)
    return bible_shape


def get_version_file_path() -> Optional[str]:
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        None,
        "Instalar versão",
        "",
        "Versões da bíblia (*.ont)"
    )
    return file_path


def install_version(file_path: str, on_update_progress: Optional[Callable] = None):
    with open(file_path) as f:
        content = f.read()

    filename = os.path.basename(file_path)
    extension = filename.split('.')[-1]

    version_name = re.sub(rf'\..+$', '', filename)
    version_dao = VersionDAO()
    version = Version(version=version_name)
    version_dao.delete_by_version_name(version.version)
    version_dao.add(version)

    try:
        bible_shape = get_bible_shape()
        verses = content_to_verses(extension, content, bible_shape, version.id)
        verse_dao = VerseDAO()
        for i, verse in enumerate(verses):
            is_last = i == len(verses) - 1
            if is_last:
                verse_dao.add(verse)
            else:
                verse_dao.add(verse, commit=False)
            if on_update_progress:
                on_update_progress((i + 1) / len(verses))

    except Exception as e:
        version_dao.delete(version.id)
        raise e


def select_file_and_install_version(on_update_progress: Optional[Callable] = None):
    file_path = get_version_file_path()
    if not file_path:
        return
    install_version(file_path, on_update_progress)
