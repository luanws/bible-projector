import os
from scripts import Script
from typing import List
from shutil import rmtree
from contextlib import suppress


def delete_empty_folders():
    directory_list: List[str] = [d[0] for d in os.walk(os.getcwd())]
    for directory in directory_list:
        with suppress(FileNotFoundError):
            subdirectory_list = os.listdir(directory)
            subdirectory_list = [
                d for d in subdirectory_list if d != '__pycache__']
            if len(subdirectory_list) == 0:
                rmtree(directory)
    print('Pastas vazias removidas com sucesso')


class DeleteEmptyFolders(Script):
    def __str__(self) -> str:
        return 'deletar pastas vazias'

    def __call__(self):
        delete_empty_folders()
