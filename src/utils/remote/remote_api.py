from flask import Flask, request, send_from_directory

from . import Remote


class RemoteAPI(Remote):
    def __init__(self) -> None:
        super().__init__()
        self.app = Flask(__name__)
        self.configure_routes()

    def _run(self) -> None:
        self.app.run(host='0.0.0.0', port=5000)

    def configure_routes(self) -> None:
        app = self.app

        @app.route('/')
        def index():
            return 'Remote API'

        @app.route('/favicon.ico')
        def favicon():
            return send_from_directory(
                app.root_path, 'icon.ico',
                mimetype='image/vnd.microsoft.icon'
            )

        @app.route('/<command>')
        def command(command: str):
            data = request.get_json()
            self.execute(command, data)
            return command
