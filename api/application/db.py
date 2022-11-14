from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from . import db

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(40))

    def __repr__(self):
        return f"{self.id} - {self.username}"
