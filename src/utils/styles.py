import json
import os
import re
from contextlib import suppress
from typing import Dict

qss_dict: Dict[str, str] = {}
qss_vars: Dict[str, str] = {}


def get_stylesheet_vars() -> Dict[str, str]:
    file_path = os.path.join('res', 'styles', 'vars.txt')
    with open(file_path) as f:
        content = f.read()
    groups = re.findall(r'(@[^\s]+)\s*=\s*([^\s]+)', content, re.MULTILINE)
    return {group[0]: group[1] for group in groups}


def apply_qss_vars(qss_vars: Dict[str, str], qss_stylesheet: str) -> str:
    stylesheet = qss_stylesheet
    for key, value in qss_vars.items():
        stylesheet = re.sub(fr'{key}\s*;', f'{value};', stylesheet)
    return stylesheet


def get_qss_dict() -> Dict[str, str]:
    file_path = os.path.join('res', 'styles', 'stylesheets.json')
    with suppress(FileNotFoundError):
        with open(file_path) as f:
            return json.load(f)
    return {}


def update_qss_dict_and_qss_vars():
    global qss_dict
    global qss_vars
    qss_vars = get_stylesheet_vars()
    qss_dict = get_qss_dict()


def check_paths_is_equal(path1: str, path2: str) -> bool:
    return os.path.abspath(path1) == os.path.abspath(path2)


def get_qss_stylesheet(qss_file_path) -> str:
    stylesheet = qss_dict[qss_file_path]
    return apply_qss_vars(qss_vars, stylesheet)
