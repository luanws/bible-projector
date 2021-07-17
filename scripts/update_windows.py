import os

from scripts import Script


class UpdateWindowsScript(Script):
    def __str__(self) -> str:
        return 'atualizar janelas do PyQt'

    def __call__(self):
        current_path = os.path.abspath(os.getcwd())

        for package in os.listdir(os.path.join(current_path, 'src', 'ui')):
            main_view_ui_path = os.path.join(
                current_path, 'src', 'ui', package, 'window.ui')
            main_view_py_path = os.path.join(
                current_path, 'src', 'ui', package, 'window.py')
            os.system(f"pyuic5 {main_view_ui_path} -o {main_view_py_path}")

        print('Janelas atualizadas com sucesso')
