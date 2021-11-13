import enum
from abc import ABC
from typing import Any, Callable, Dict, Union

from PyQt5.QtCore import QRunnable, QThreadPool


class Command(enum.Enum):
    SEARCH_BY_REFERENCE = 'search_by_reference'


class Remote(QRunnable):
    commands: Dict[Command, Callable[[Any], None]]

    def __init__(self) -> None:
        self.commands = {}

    def start(self) -> None:
        pool = QThreadPool.globalInstance()
        pool.start(self)

    def run(self) -> None:
        pass

    def add_command_listener(self, command: Command, callable: Callable[[Any], None]) -> None:
        self.commands[command] = callable

    def execute(self, command: Union[Command, str], data: Any = None) -> None:
        command = Command(command)
        if command in self.commands:
            self.commands[command](data)
