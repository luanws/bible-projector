from typing import List

from src.utils import styles
from src.utils.settings.theme_settings import ThemeSettings


class ThemeSettingsViewModel:
    theme_settings: ThemeSettings

    def __init__(self) -> None:
        self.theme_settings = ThemeSettings()

    @property
    def current_theme(self) -> str:
        return self.theme_settings.theme

    @property
    def themes(self) -> List[str]:
        return styles.get_themes()

    def change_theme(self, theme: str) -> None:
        self.theme_settings.theme = theme
        self.theme_settings.save()
