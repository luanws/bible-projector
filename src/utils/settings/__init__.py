from __future__ import annotations

from abc import ABC
from configparser import ConfigParser
from contextlib import suppress
from typing import Any, Callable, Dict, List, Optional, Tuple


def filter_dict_not_starts_with_underscore(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if not k.startswith('_')}


class Settings(ABC):
    config: ConfigParser = ConfigParser()
    settings_instances: Dict[str,
                             List[Tuple[Settings, Optional[Callable]]]] = {}

    def __init__(self, on_change_settings: Optional[Callable] = None) -> None:
        super().__init__()
        self.__add_setting_instance(on_change_settings)
        self.__load_config()
        self.__load_config_by_defaults()
        self.__init_subclass()

    def __add_setting_instance(self, on_change_settings: Optional[Callable]):
        if not Settings.settings_instances.__contains__(self.__class__.__name__):
            Settings.settings_instances[self.__class__.__name__] = []
        Settings.settings_instances[self.__class__.__name__].append(
            (self, on_change_settings))

    def __load_config(self):
        if not Settings.config.sections():
            Settings.config.read('config.ini')

    def __load_config_by_defaults(self):
        if not Settings.config.sections().__contains__(self.__class__.__name__):
            cls = self.__class__
            config_dict = filter_dict_not_starts_with_underscore(cls.__dict__)
            Settings.config[cls.__name__] = config_dict

    def __init_subclass(self):
        with suppress(KeyError):
            section = Settings.config[self.__class__.__name__]
            config_dict: Dict[str, Any] = dict(section)
            self.from_dict(config_dict)

    def save(self):
        Settings.config[self.__class__.__name__] = self.to_dict()
        self.update_settings_instances()
        self.notify_settings_instances()
        with open('config.ini', 'w') as file:
            Settings.config.write(file)

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__

    def from_dict(self, config_dict: Dict[str, Any]):
        for k, v in self.__annotations__.items():
            config_dict[k] = v(config_dict[k])
        self.__dict__ = config_dict

    def update_settings_instances(self):
        for setting_instance, _ in Settings.settings_instances[self.__class__.__name__]:
            if setting_instance is not self:
                setting_instance.from_dict(self.to_dict().copy())

    def notify_settings_instances(self):
        for _, on_change_settings in Settings.settings_instances[self.__class__.__name__]:
            if on_change_settings is not None:
                on_change_settings()
