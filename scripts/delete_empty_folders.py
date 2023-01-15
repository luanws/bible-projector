import os
from contextlib import suppress
from shutil import rmtree
from typing import List


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


if __name__ == '__main__':
    delete_empty_folders()
