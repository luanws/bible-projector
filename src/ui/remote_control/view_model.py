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

        self.remote_api.add_command_listener(
            Command.SEARCH_BY_REFERENCE,
            self.search_by_reference
        )

    def search_by_reference(self, data: Dict[str, Any]) -> None:
        reference = data['reference']
        print(reference)
        self.main_window_control.search(reference)

    def start_api(self) -> str:
        self.remote_api.start()
        return self.remote_api.address
