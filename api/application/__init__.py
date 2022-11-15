import os
from sqlite3 import OperationalError
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('application.config.DevelopmentConfig')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        from . import auth, errors, database
        db = database.engine
        database.Base.metadata.create_all(db)
        app.register_blueprint(auth.bp)
        app.register_error_handler(400, errors.handle_bad_request)
        app.register_error_handler(422, errors.handle_unprocessable_entity)

    return app
