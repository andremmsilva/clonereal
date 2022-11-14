import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('application.config.DevelopmentConfig')

    db = SQLAlchemy(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        from . import auth
        app.register_blueprint(auth.bp)
        db.create_all()

    return app
