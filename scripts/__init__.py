from __future__ import annotations

import sys
from abc import ABC
from typing import List, Type

from pymenu import Menu


def run_command(scripts: List[Type[Script]], command: str):
    if command.isnumeric():
        return scripts[int(command) - 1]()
    raise Exception('Comando inválido')


class Script(ABC):
    def __init__(self) -> None:
        pass

    @classmethod
    def start(cls):
        scripts = [c() for c in cls.__subclasses__()]
        commands = sys.argv[1:]
        if len(commands) == 0:
            menu = Menu('Menu')
            menu.add_options([(str(s), s) for s in scripts])
            menu.show()
        for command in commands:
            run_command(scripts, command)
