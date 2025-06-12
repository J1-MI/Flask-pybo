from flask import Blueprint

bp = Blueprint('hello_world', __name__, url_prefix='/hello_world')

@bp.route('/')
def hello_world():
    return 'Hello, World!'