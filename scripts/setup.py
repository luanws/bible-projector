import os
import shutil
import traceback
from contextlib import suppress
from typing import List, Tuple

import PyInstaller.__main__
from src.version import version

from scripts import Script

application_name = 'Projetor bíblico'

assets_path = os.path.join('data')
dist_path = os.path.join('dist')
portable_path = os.path.join(dist_path, application_name)
zip_path = os.path.join(dist_path, f'{application_name} {version}')

copy_files = [
    ('icon.ico', portable_path),
]

copy_folders = [
    ('data', os.path.join(portable_path, 'data')),
    ('res', os.path.join(portable_path, 'res')),
]


def clear_build(application_name: str):
    with suppress(FileNotFoundError):
        shutil.rmtree('build')

    with suppress(FileNotFoundError):
        os.remove(f'{application_name}.spec')


def copy_assets(copy_files: List[Tuple[str, str]], copy_folders: List[Tuple[str, str]]):
    for source, target in copy_files:
        shutil.copy(source, target)

    for source, target in copy_folders:
        with suppress(FileNotFoundError):
            shutil.rmtree(target)
        shutil.copytree(source, target)


def zip_portable(target_path: str, source_path: str):
    shutil.make_archive(target_path, 'zip', source_path)


def run_pyinstaller(application_name: str, dist_path: str):
    PyInstaller.__main__.run([
        'main.py',
        '--name=%s' % application_name,
        '--icon=icon.ico',
        '--onefile',
        '--windowed',
        '--distpath=%s' % dist_path,
    ])


def setup():
    try:
        run_pyinstaller(application_name, portable_path)
        copy_assets(copy_files, copy_folders)
        zip_portable(zip_path, portable_path)
    except:
        traceback.print_exc()
    finally:
        clear_build(application_name)


class SetupScript(Script):
    def __str__(self) -> str:
        return 'setup'

    def __call__(self):
        setup()
