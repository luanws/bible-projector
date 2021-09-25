from __future__ import annotations

from abc import ABC
from configparser import ConfigParser
from contextlib import suppress
from typing import Any, Dict


def filter_dict_not_starts_with_underscore(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if not k.startswith('_')}


class Settings(ABC):
    config: ConfigParser = ConfigParser()

    def __init__(self) -> None:
        super().__init__()
        self.__load_config()
        self.__load_config_by_defaults()
        self.init_subclass()

    def __load_config(self):
        if not Settings.config.sections():
            Settings.config.read('config.ini')

    def __load_config_by_defaults(self):
        if not Settings.config.sections().__contains__(self.__class__.__name__):
            cls = self.__class__
            config_dict = filter_dict_not_starts_with_underscore(cls.__dict__)
            Settings.config[cls.__name__] = config_dict

    def init_subclass(self):
        with suppress(KeyError):
            section = Settings.config[self.__class__.__name__]
            config_dict: Dict[str, Any] = dict(section)
            self.from_dict(config_dict)

    def save(self):
        Settings.config[self.__class__.__name__] = self.to_dict()
        with open('config.ini', 'w') as file:
            Settings.config.write(file)

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__

    def from_dict(self, config_dict: Dict[str, Any]):
        self.__dict__ = config_dict
