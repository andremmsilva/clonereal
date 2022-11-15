from flask import jsonify
from werkzeug.exceptions import BadRequest, UnprocessableEntity


def handle_bad_request(e: BadRequest):
    return jsonify({"Error": e.description}), 400


def handle_unprocessable_entity(e: UnprocessableEntity):
    return jsonify({"Error": e.description}), 422
