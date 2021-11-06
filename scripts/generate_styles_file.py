import json
import os
from typing import Dict, List

from termcolor import cprint

from scripts import Script


def get_all_file_paths_with_extension(extension: str) -> List[str]:
    file_paths: List[str] = []
    for root, dirs, file_names in os.walk('.'):
        for file_name in file_names:
            if file_name.endswith(extension):
                file_path = os.path.join(root, file_name)
                file_paths.append(file_path)
    return file_paths


def format_qss_file_path(qss_file_path: str) -> str:
    file_path = qss_file_path.replace(os.path.sep, '/')
    if file_path.startswith('./'):
        file_path = file_path[2:]
    return file_path


def read_qss_file(qss_file_path: str) -> str:
    with open(qss_file_path) as qss_file:
        return qss_file.read()


def qss_file_paths_to_dict(qss_file_paths: List[str]) -> Dict[str, str]:
    qss_file_paths_dict: Dict[str, str] = {}
    for qss_file_path in qss_file_paths:
        qss_file_path_key = format_qss_file_path(qss_file_path)
        qss_file_path_value = read_qss_file(qss_file_path)
        qss_file_paths_dict[qss_file_path_key] = qss_file_path_value
    return qss_file_paths_dict


def save_qss_dict_as_styles_file(qss_dict: Dict[str, str]):
    with open('styles.json', 'w') as styles_file:
        json.dump(qss_dict, styles_file)


def generate_styles_file():
    qss_file_paths = get_all_file_paths_with_extension('.qss')
    qss_dict = qss_file_paths_to_dict(qss_file_paths)
    print(f'Found {len(qss_file_paths)} qss files:')
    for qss_file_path in qss_dict.keys():
        cprint(qss_file_path, 'blue')
    save_qss_dict_as_styles_file(qss_dict)
    cprint('Arquivos de estilos gerado com sucesso', 'green')


class GenerateStylesFile(Script):
    def __str__(self) -> str:
        return 'gerar arquivo de estilos'

    def __call__(self):
        generate_styles_file()
