from flask import Flask
from werkzeug.serving import make_server


class Server:
    def __init__(self, app: Flask, host: str, port: int):
        self.server = make_server(host, port, app)
        self.context = app.app_context()
        self.context.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()
