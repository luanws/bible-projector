import random
import socket
import string
from typing import Optional


def generate_random_string_with_letters_and_digits(length: int) -> str:
    return ''.join(random.choices(
        string.ascii_letters + string.digits,
        k=length
    ))


def get_host() -> str:
    return socket.gethostbyname(socket.gethostname())


class ServerAddress:
    host: str
    port: int
    prefix: str

    def __init__(self, port: int) -> None:
        self.port = port
        self.host = get_host()
        self.prefix = ''

    def generate_prefix(self, length: int) -> str:
        self.prefix = generate_random_string_with_letters_and_digits(length)
        return self.prefix

    @property
    def address(self) -> str:
        if not self.prefix:
            return f'{self.host}:{self.port}'
        return f'http://{self.host}:{self.port}/{self.prefix}'

    @property
    def localhost_address(self) -> str:
        if not self.prefix:
            return f'http://localhost:{self.port}'
        return f'http://localhost:{self.port}/{self.prefix}'
