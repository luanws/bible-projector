from typing import Any, Dict

from src.ui.main.control import MainWindowControl
from src.utils.remote import Command
from src.utils.remote.remote_api import RemoteAPI


class RemoteControlViewModel:
    remote_api: RemoteAPI
    main_window_control: MainWindowControl

    def __init__(self, main_window_control: MainWindowControl) -> None:
        self.main_window_control = main_window_control

        self.remote_api = RemoteAPI(prefix_length=40)

        commands = [
            (Command.SEARCH_BY_REFERENCE, self.search_by_reference),
            (Command.PREVIOUS_VERSE, self.previous_verse),
            (Command.NEXT_VERSE, self.next_verse),
        ]
        for command, callback in commands:
            self.remote_api.add_command_listener(command, callback)

    def search_by_reference(self, data: Dict[str, Any]) -> None:
        reference = data['reference']
        self.main_window_control.search(reference)

    def previous_verse(self, data: Dict[str, Any]) -> None:
        self.main_window_control.previous_verse()

    def next_verse(self, data: Dict[str, Any]) -> None:
        self.main_window_control.next_verse()

    def start_api(self) -> str:
        self.remote_api.start()
        return self.remote_api.address
