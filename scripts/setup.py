import os
import shutil
import traceback
from contextlib import suppress

import PyInstaller.__main__

from scripts import Script

application_name = 'Projetor bíblico'

assets_path = os.path.join('data')
dist_path = os.path.join('dist')

copy_files = [
    ('icon.ico', dist_path),
]

copy_folders = [
    ('data', os.path.join(dist_path, 'data')),
    ('res', os.path.join(dist_path, 'res')),
]


def setup():
    try:
        PyInstaller.__main__.run([
            'main.py',
            '--name=%s' % application_name,
            '--icon=icon.ico',
            '--onefile',
            '--windowed',
        ])

        for source, destination in copy_files:
            shutil.copy(source, destination)

        for source, destination in copy_folders:
            with suppress(FileNotFoundError):
                shutil.rmtree(destination)
            shutil.copytree(source, destination)
    except:
        traceback.print_exc()
    finally:
        with suppress(FileNotFoundError):
            shutil.rmtree('build')

        with suppress(FileNotFoundError):
            os.remove(f'{application_name}.spec')


class SetupScript(Script):
    def __str__(self) -> str:
        return 'setup'

    def __call__(self):
        setup()
