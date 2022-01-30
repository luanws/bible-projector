from __future__ import annotations

import inspect
from abc import ABC
from collections import defaultdict
from configparser import ConfigParser
from contextlib import suppress
from typing import Any, Callable, Dict, Optional


def nested_dict(): return defaultdict(nested_dict)


def filter_dict_not_starts_with_underscore(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if not k.startswith('_')}


def get_class_attributes(cls: type) -> Dict[str, Any]:
    return dict(inspect.getmembers(cls, lambda m: not inspect.isroutine(m)))


class Settings(ABC):
    CONFIG_FILE_NAME = 'config.ini'
    config: ConfigParser = ConfigParser()
    settings_instances: Dict[str, Dict[Settings,
                                       Optional[Callable]]] = nested_dict()

    def __init__(self) -> None:
        super().__init__()
        self.__load_config()
        self.__load_config_by_defaults()
        self.__init_subclass()
        self.__register_instance()

    def __load_config(self):
        if not Settings.config.sections():
            Settings.config.read(Settings.CONFIG_FILE_NAME)

    def __load_config_by_defaults(self):
        if not Settings.config.sections().__contains__(self.__class__.__name__):
            cls = self.__class__
            settings_attributes = get_class_attributes(Settings)
            config_dict = get_class_attributes(cls)
            config_dict = filter_dict_not_starts_with_underscore(config_dict)
            config_dict = {k: v for k, v in config_dict.items()
                           if k not in settings_attributes}
            Settings.config[cls.__name__] = config_dict

    def __init_subclass(self):
        with suppress(KeyError):
            section = Settings.config[self.__class__.__name__]
            config_dict: Dict[str, Any] = dict(section)
            self.from_dict(config_dict)

    def __register_instance(self):
        class_name = self.__class__.__name__
        Settings.settings_instances[class_name][self] = None

    def before_notify_settings_instances(self):
        pass

    def save(self):
        Settings.config[self.__class__.__name__] = self.to_dict()
        self.update_settings_instances()
        self.notify_settings_instances()
        with open(Settings.CONFIG_FILE_NAME, 'w') as file:
            Settings.config.write(file)

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__

    def from_dict(self, config_dict: Dict[str, Any]):
        for k, v in self.__annotations__.items():
            config_dict[k] = v(config_dict[k])
        self.__dict__ = config_dict

    def update_settings_instances(self):
        class_name = self.__class__.__name__
        for setting_instance in Settings.settings_instances[class_name]:
            if setting_instance is not self:
                setting_instance.from_dict(self.to_dict().copy())

    def notify_settings_instances(self):
        self.before_notify_settings_instances()
        for on_change_settings in dict(Settings.settings_instances[self.__class__.__name__]).values():
            if on_change_settings is not None:
                on_change_settings()

    def on_change_settings(self, callable: Callable):
        class_name = self.__class__.__name__
        Settings.settings_instances[class_name][self] = callable
