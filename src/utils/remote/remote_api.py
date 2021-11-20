from typing import Any, Optional

from flask import Flask, request, send_from_directory
from werkzeug.serving import make_server

from . import Remote


class Server:
    def __init__(self, app: Flask):
        self.server = make_server('0.0.0.0', 5000, app)
        self.context = app.app_context()
        self.context.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()


class RemoteAPI(Remote):
    def __init__(self) -> None:
        super().__init__()
        self.app = Flask(__name__)
        self.server = Server(self.app)
        self.configure_routes()

    def _run(self) -> None:
        self.server.run()

    def stop(self) -> None:
        self.server.shutdown()

    def configure_routes(self) -> None:
        app = self.app

        @app.route('/')
        def index():
            return 'Remote API'

        @app.route('/favicon.ico')
        def favicon():
            return send_from_directory(
                app.root_path, 'icon.ico',
            )

        @app.route('/<command>')
        def command(command: str):
            data = request.get_json()
            self.execute(command, data)
            return command
