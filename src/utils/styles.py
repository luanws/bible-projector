import json
import os
from typing import Dict

qss_dict: Dict[str, str] = {}


def get_qss_dict() -> Dict[str, str]:
    file_path = os.path.join('data', 'styles.json')
    with open(file_path) as f:
        return json.load(f)


def update_qss_dict():
    global qss_dict
    qss_dict = get_qss_dict()


def check_paths_is_equal(path1: str, path2: str) -> bool:
    return os.path.abspath(path1) == os.path.abspath(path2)


def get_qss_stylesheet(qss_file_path) -> str:
    return qss_dict[qss_file_path]
