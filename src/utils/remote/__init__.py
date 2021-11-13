import enum
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Union


class Command(enum.Enum):
    SEARCH_BY_REFERENCE = 'search_by_reference'


class Remote(ABC):
    commands: Dict[Command, Callable[[Any], None]]

    def __init__(self) -> None:
        self.commands = {}

    def add_command_listener(self, command: Command, callable: Callable[[Any], None]) -> None:
        self.commands[command] = callable

    def execute(self, command: Union[Command, str], data) -> None:
        command = Command(command)
        if command in self.commands:
            self.commands[command](data)
