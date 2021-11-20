from typing import Any, Dict

from src.utils.remote import Command
from src.utils.remote.remote_api import RemoteAPI


class RemoteControlViewModel:
    remote_api: RemoteAPI

    def __init__(self) -> None:
        self.remote_api = RemoteAPI(prefix_length=40)

        self.remote_api.add_command_listener(
            Command.SEARCH_BY_REFERENCE,
            self.search_by_reference
        )

    def search_by_reference(self, data: Dict[str, Any]) -> None:
        print(data)
    
    def start_api(self) -> str:
        self.remote_api.start()
        return self.remote_api.address
