import json
import os
import re
from typing import Dict

from PyQt5 import QtWidgets
from src.dao.verse_dao import VerseDAO
from src.dao.version_dao import VersionDAO
from src.models.version import Version

from .parsers import ont_to_verses


def get_bible_shape() -> Dict[str, Dict[str, int]]:
    with open('data/bible_shape.json') as f:
        bible_shape = json.load(f)
    return bible_shape


def get_version_file_path() -> str:
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        None,
        "Instalar versão",
        "",
        "Versões da bíblia (*.ont)"
    )
    return file_path


def install_version(file_path: str):
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

        parsers_dict = {
            'ont': ont_to_verses,
        }
        parser = parsers_dict[extension]
        verses = parser(content, bible_shape, version.id)
        verse_dao = VerseDAO()
        verse_dao.add_many(verses)
    except Exception as e:
        version_dao.delete(version.id)
        raise e


def select_file_and_install_version():
    file_path = get_version_file_path()
    install_version(file_path)
