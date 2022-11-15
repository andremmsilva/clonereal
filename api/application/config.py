from pathlib import Path


class DevelopmentConfig:
    SECRET_KEY = "dev"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        str(Path(__file__).parent.absolute()) + "/nowsound.db"
