import string as Str
from flask import current_app
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from werkzeug.exceptions import UnprocessableEntity

Base = declarative_base()

engine = create_engine(
    current_app.config["SQLALCHEMY_DATABASE_URI"], echo=True, future=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(40))
    password = Column(String(64))

    def __repr__(self):
        return f"{self.id} - {self.username}"

    def assert_valid_credentials(self):
        if not User.valid_username(self.username) or not User.valid_password(self.password):
            raise UnprocessableEntity("Invalid username or password")

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            if column.name not in User.dont_serialize():
                d[column.name] = str(getattr(self, column.name))
        return d

    @staticmethod
    def dont_serialize():
        return set(["password"])

    @staticmethod
    def valid_username(username: str) -> bool:
        """Validates a given username.

        Args:
            username (str)

        Returns:
            bool: True if the username consists of only letters and numbers and is longer than 3 characters.
        """
        return username.isalnum() and len(username) > 3

    @staticmethod
    def valid_password(password: str) -> bool:
        """Validates a given password. Must contain at least 8 characters, consisting of letters, digits and punctuation.

        Args:
            password (str)

        Returns:
            bool: True if the password matches the criteria.
        """
        letters = 0
        digits = 0
        specials = 0
        if len(password) > 8:
            for l in password:
                if l in Str.ascii_letters:
                    letters += 1
                elif l in Str.digits:
                    digits += 1
                elif l in Str.punctuation:
                    specials += 1
                else:
                    return False
            arr = [letters, digits, specials]
            return all(arr[i] > 0 for i in range(3))
        return False
