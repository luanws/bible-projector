from flask import Flask

from . import Remote


class RemoteAPI(Remote):
    def __init__(self) -> None:
        super().__init__()
        self.app = Flask(__name__)
        self.configure_routes()

    def run(self) -> None:
        self.app.run(host='0.0.0.0', port=5000)

    def configure_routes(self) -> None:
        app = self.app

        @app.route('/')
        def index():
            return 'Remote API'

        @app.route('/<command>')
        def command(command: str):
            self.execute(command)
            return command
