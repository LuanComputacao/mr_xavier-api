from flask import Flask
from environs import Env
import os
from flask_migrate import Migrate

from app.views import home, questions, items


env = Env()
env.read_env()

db_file = env('SQLALCHEMY_DATABASE_URI')
db_path = os.path.join(os.getcwd(), db_file)
db_file_uri = f'sqlite:///{db_path}'


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_file_uri


    from app.models import db
    migrate = Migrate(app, db)
    db.init_app(app)

    app.register_blueprint(home.bp)
    app.register_blueprint(questions.bp)
    app.register_blueprint(items.bp)

    return app
