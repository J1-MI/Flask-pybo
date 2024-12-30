from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, pybo!'

@bp.route('/')
def index():
    current_app.logger.info("Output at INFO level")
    return redirect(url_for('question._list')) #question, _list 순서로 해석되어 라우팅 함수 파인딩

