from flask import Blueprint, request, jsonify, session
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, Unauthorized
from .database import User, engine

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["POST"])
def register():
    """Registers a new user.

    Raises:
        BadRequest: If the request is not JSON or doesn't have the required fields.
        UnprocessableEntity: If the username or password are invalid.

    Returns:
        The username and 201 Created code.
    """
    data = request.get_json()

    if "username" not in data or "password" not in data:
        raise BadRequest()

    user = User(username=data["username"], password=data["password"])
    user.assert_valid_credentials()

    user.password = generate_password_hash(user.password)

    with Session(engine) as db:
        db.add(user)
        db.commit()
        session["user"] = user.to_dict()
        return jsonify(user.to_dict()), 201


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if "username" not in data or "password" not in data:
        raise BadRequest()

    username = data["username"]
    if User.valid_username(username):
        with Session(engine) as db:
            try:
                user: User = db.query(User).filter(
                    User.username == username).one()
                if check_password_hash(user.password, data["password"]):
                    session["user"] = user.to_dict()
                    return jsonify(user.to_dict()), 200
                else:
                    raise Unauthorized("Invalid username or password.")
            except NoResultFound:
                # No user with that name.
                raise Unauthorized("Invalid username or password.")


@bp.route("/logout", methods=["POST"])
def logout():
    user = session.get("user")
    if not user:
        raise Unauthorized()
    session.pop("user")
    return "", 204
