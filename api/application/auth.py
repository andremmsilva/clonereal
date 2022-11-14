from flask import Blueprint, request, jsonify

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']

    return jsonify({"username": username})
