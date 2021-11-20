from typing import Optional

from flask import Flask
from src.utils.remote import Remote

from . import routes
from .server import Server
from .server_address import ServerAddress


class RemoteAPI(Remote):
    __app: Flask
    __server: Server
    __server_address: ServerAddress
    prefix_length: int

    def __init__(self, parent=None, prefix_length: int = 0) -> None:
        super().__init__(parent=parent)
        self.prefix_length = prefix_length

    @property
    def address(self) -> str:
        return self.__server_address.address

    def start(self) -> None:
        self.__app = Flask(__name__)
        self.__server_address = ServerAddress(port=5000)
        self.__server_address.generate_prefix(self.prefix_length)
        print(f'Server prefix: {self.__server_address.prefix}')
        return super().start()

    def _run(self) -> None:
        self.__server = Server(
            self.__app, '0.0.0.0',
            self.__server_address.port
        )
        self.configure_routes()
        print(f'Starting server on {self.__server_address.localhost_address}')
        print(f'Starting server on {self.__server_address.address}')
        self.__server.run()

    def stop(self) -> None:
        self.__server.stop()
        print('Server stopped')

    def configure_routes(self) -> None:
        routes.execute = self.execute
        self.__app.register_blueprint(
            routes.api_routes_blueprint,
            url_prefix=f'/{self.__server_address.prefix}'
        )
