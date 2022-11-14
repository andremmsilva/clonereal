from pathlib import Path

class DevelopmentConfig:
    SECRET_KEY = "dev"
    SQLALCHEMY_DATABASE_URI = "sqlite:///"

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI += str(Path(__file__).parent.absolute()) + "nowsound.db"

