import subprocess
from contextlib import suppress
from typing import Dict, List


def get_installed_packages() -> List[str]:
    return subprocess.check_output(['pip', 'freeze']).decode('utf-8').splitlines()


def install_package(package: str):
    with suppress(Exception):
        subprocess.call(['pip', 'install', package])


def install_packages(packages: List[str]):
    for package in packages:
        install_package(package)


def get_packages(filename: str):
    with open(filename, 'rb') as file:
        content = file.read().decode('utf-16')
        return content.splitlines()


def save_packages(filename: str, packages: List[str]):
    with open(filename, 'w') as file:
        file.write('\n'.join(packages))


def save_log(filename: str, packages_dict: Dict[str, List[str]]):
    with open(filename, 'w') as file:
        for title, packages in packages_dict.items():
            if len(packages) == 0:
                continue
            file.write(f'{title}\n')
            file.write('\n'.join(packages))
            file.write('\n\n')


def get_flags_from_args(args: List[str]) -> Dict[str, str]:
    flags: Dict[str, str] = {}
    for arg in args:
        if arg.startswith('-'):
            if '=' in arg:
                key, value = arg.split('=')
                flags[key] = value
            else:
                flags[arg] = ''
            args.remove(arg)
    return flags


def install():
    filename = input('Digite o nome do arquivo de dependências [requirements.txt]: ') or 'requirements.txt'
    log_only = input('Somente gerar log? [y/n]: ').lower() == 'y'
    packages = get_packages(filename)
    if not log_only:
        install_packages(packages)
    installed_packages = get_installed_packages()
    not_installed_packages = [p for p in packages if p not in installed_packages]
    extra_packages = [p for p in installed_packages if p not in packages]
    success_packages = [p for p in packages if p in installed_packages]
    save_log(f'{filename}.log', {
        'Success packages'.upper(): success_packages,
        'Not installed packages'.upper(): not_installed_packages,
        'Extra packages'.upper(): extra_packages,
    })


if __name__ == '__main__':
    install()
