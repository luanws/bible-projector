from typing import Any, Callable, Dict, Optional, Union

from flask import Blueprint, request
from src.utils.remote import Command
from werkzeug.utils import send_from_directory

api_routes_blueprint = Blueprint('api_routes', __name__)

execute: Callable[[Union[Command, str], Optional[Dict[str, Any]]], None]


@api_routes_blueprint.route('/')
def index():
    return 'Remote API'


@api_routes_blueprint.route('/favicon.ico')
def favicon():
    return send_from_directory(
        api_routes_blueprint.root_path, 'icon.ico',
    )


@api_routes_blueprint.route('/<command>')
def command(command: str):
    global execute
    data = request.get_json()
    execute(command, data)
    return command
