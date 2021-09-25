from __future__ import annotations

from abc import ABC
from configparser import ConfigParser
from contextlib import suppress
from typing import Any, Dict, List


def filter_dict_by_keys(d: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if k in keys}


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
        if not Settings.config.sections():
            cls = self.__class__
            keys = cls.__annotations__.keys()
            config_dict = filter_dict_by_keys(cls.__dict__, keys)
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
