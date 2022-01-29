import sys
from scripts.generate_styles_file import GenerateStylesFile
from scripts.update_windows import UpdateWindowsScript


def except_hook(cls, exception, traceback):
    traceback.print_exc()


if __name__ == '__main__':
    sys.excepthook = except_hook

    UpdateWindowsScript()()
    GenerateStylesFile()()

    from main import main
    main()
