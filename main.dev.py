from scripts.generate_styles_file import GenerateStylesFile
from scripts.update_windows import UpdateWindowsScript

if __name__ == '__main__':
    UpdateWindowsScript()()
    GenerateStylesFile()()

    from main import main
    main()
