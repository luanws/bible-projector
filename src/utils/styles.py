import os


def get_qss_stylesheet(qss_file) -> str:
    file_path = os.path.join(os.getcwd(), 'src', 'styles', f'{qss_file}.qss')
    with open(file_path, 'r') as f:
        return f.read()
