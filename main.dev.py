import sys

from scripts.generate_styles_file import generate_styles_file
from scripts.update_windows import update_windows


def except_hook(cls, exception, traceback):
    traceback.print_exc()


if __name__ == '__main__':
    sys.excepthook = except_hook

    update_windows()
    generate_styles_file()

    from main import main
    main()
