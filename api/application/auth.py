from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from werkzeug.exceptions import BadRequest
from .database import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=['POST'])
def register():
    """Registers a new user.

    Raises:
        BadRequest: If the request is not JSON or doesn't have the required fields.
        UnprocessableEntity: If the username or password are invalid.

    Returns:
        The username and 201 Created code.
    """
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        raise BadRequest()

    user = User(username=data['username'], password=data['password'])
    user.assert_valid_credentials()

    user.password = generate_password_hash(user.password)

    return jsonify({"username": user.username}), 201
