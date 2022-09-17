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


assets_to_copy = [
    ('icon.ico', portable_path),
    ('data', os.path.join(portable_path, 'data')),
    ('res', os.path.join(portable_path, 'res')),
]


def remove_path(path: str):
    with suppress(FileNotFoundError):
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)


def clear_build(application_name: str):
    remove_path('build')
    remove_path(f'{application_name}.spec')


def copy_assets(assets: List[Tuple[str, str]]):
    for source, target in assets:
        if os.path.isfile(source):
            shutil.copy(source, target)
        elif os.path.isdir(source):
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
        remove_path(portable_path)
        run_pyinstaller(application_name, portable_path)
        copy_assets(assets_to_copy)
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
