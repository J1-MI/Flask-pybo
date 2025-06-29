from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def page_not_found(e):
    return render_template('404.html'), 404

def create_app(): #애플리케이션 팩토리(application factory)
    app = Flask(__name__) #app 객체 생성 및 반환
    app.config.from_envvar('APP_CONFIG_FILE')

    #Error Page
    app.register_error_handler(404, page_not_found)

    #ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    #Blueprint
    from .views import main_views, question_views, answer_views, auth_views, cbt_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(cbt_views.bp)

    #Filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    #Markdown
    from markdown import markdown

    @app.template_filter('markdown')
    def markdown_filter(content):
        return markdown(content, extensions=['nl2br', 'fenced_code'])

    #hello, world!
    from .views import hello_world
    app.register_blueprint(hello_world.bp)

    return app
