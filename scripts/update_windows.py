import os
import re
from typing import List, Tuple

from scripts import Script


def get_file_name_and_roots(directory: str, pattern: str) -> List[Tuple[str, str]]:
    file_name_and_roots: List[Tuple[str, str]] = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if re.match(pattern, filename):
                file_name_and_roots.append((root, filename))
    return file_name_and_roots


def remove_comments_from_python_file(path: str):
    with open(path) as file:
        content = file.read()

    content = re.sub(r'^#.*', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\n+', '', content, flags=re.MULTILINE)

    with open(path, 'w') as file:
        file.write(content)


class UpdateWindowsScript(Script):
    def __str__(self) -> str:
        return 'atualizar janelas do PyQt'

    def __call__(self):
        for root, ui_file_name in get_file_name_and_roots('src', r'.+\.ui$'):
            filename = os.path.splitext(ui_file_name)[0]
            ui_file_path = os.path.join(root, ui_file_name)
            py_file_path = os.path.join(root, f'{filename}.py')
            os.system(f"pyuic5 {ui_file_path} -o {py_file_path}")
            remove_comments_from_python_file(py_file_path)

        print('Janelas atualizadas com sucesso')
