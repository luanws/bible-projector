from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import MainWindow


class MainWindowControl:
    main_window: 'MainWindow'

    def __init__(self, main_window: 'MainWindow') -> None:
        self.main_window = main_window

    def search(self, search_text: str) -> None:
        self.main_window.search(search_text)

    def previous_verse(self) -> None:
        self.main_window.previous_verse()

    def next_verse(self) -> None:
        self.main_window.next_verse()
