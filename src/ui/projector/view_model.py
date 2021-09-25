from typing import Callable, Optional

from src.utils.settings.projector_font_settings import ProjectorFontSettings


class ProjectorViewModel:
    __text: str
    __on_change_text_callable: Optional[Callable[[str], None]] = None
    font_settings: ProjectorFontSettings

    def __init__(self) -> None:
        self.__text: str = ''
        self.font_settings = ProjectorFontSettings()

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text
        if self.__on_change_text_callable is not None:
            self.__on_change_text_callable(text)

    def on_change_text(self, callable: Callable[[str], None]):
        self.__on_change_text_callable = callable
