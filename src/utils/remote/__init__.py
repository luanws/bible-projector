import enum
import threading
from abc import abstractmethod
from typing import Any, Callable, Dict, Optional, Union

from PyQt5 import QtCore


class Command(enum.Enum):
    SEARCH_BY_REFERENCE = 'search_by_reference'


class Remote(QtCore.QObject):
    commands: Dict[Command, Callable[[Any], None]] = {}
    __command_received = QtCore.pyqtSignal(Command, str)

    def __init__(self, parent: Optional[QtCore.QObject] = None) -> None:
        super().__init__(parent=parent)
        self.__command_received.connect(self.__on_command_received)

    def run(self) -> None:
        threading.Thread(target=self._run).start()

    @abstractmethod
    def _run(self) -> None:
        pass

    def __on_command_received(self, command: Command, data: str) -> None:
        if command in self.commands:
            self.commands[command](data)

    def add_command_listener(self, command: Command, callable: Callable[[Any], None]) -> None:
        self.commands[command] = callable

    def execute(self, command: Union[Command, str], data: str = None) -> None:
        command = Command(command)
        if command in self.commands:
            self.__command_received.emit(command, data)
