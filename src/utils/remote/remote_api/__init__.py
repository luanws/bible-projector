from flask import Flask
from src.utils.remote import Remote

from . import routes
from .server import Server


class RemoteAPI(Remote):
    def __init__(self) -> None:
        super().__init__()
        self.__app = Flask(__name__)
        self.__server = Server(self.__app, '0.0.0.0', 5000)
        self.configure_routes()

    def _run(self) -> None:
        self.__server.run()

    def stop(self) -> None:
        self.__server.shutdown()

    def configure_routes(self) -> None:
        routes.execute = self.execute
        self.__app.register_blueprint(routes.api_routes_blueprint)
