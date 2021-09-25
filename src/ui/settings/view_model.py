from src.utils.settings.projector_font_settings import ProjectorFontSettings


class SettingsViewModel:
    projector_font_settings: ProjectorFontSettings

    def __init__(self) -> None:
        self.projector_font_settings = ProjectorFontSettings()

    def save_settings(self) -> None:
        self.projector_font_settings.save()

    def change_projector_font_size(self, new_size: int) -> None:
        self.projector_font_settings.font_size = new_size
