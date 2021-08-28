import os
import shutil
import traceback
from contextlib import suppress

import PyInstaller.__main__

from scripts import Script

application_name = 'Projetor bíblico'

assets_folder_path = os.path.join('data')
dist_folder_path = os.path.join('dist')


def setup():
    try:
        PyInstaller.__main__.run([
            'main.py',
            '--name=%s' % application_name,
            '--icon=icon.ico',
            '--onefile',
            '--windowed',
        ])
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
