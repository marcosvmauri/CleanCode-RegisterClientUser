from flask import Blueprint, jsonify, request
from src.main.adapter.api_adapter import flask_adapter
from src.main.composer import (
    register_user_composer,
    register_client_composer,
    find_client_composer,
    find_user_composer,
)

api_routes_bp = Blueprint("api_routes", __name__)

@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """ register user route """

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributest": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/clients", methods=["POST"])
def register_clients():
    """ register clients route """

    message = {}
    response = flask_adapter(request=request, api_route=register_client_composer())

    if response.status_code < 300:
        message = {
            "type": "clients",
            "id": response.body.id,
            "attributest": {
                "name": response.body.name
            },
            "relationships": {"owner": {"type": "users", "id": response.body.user_id}},
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/clients", methods=["GET"])
def finder_clients():
    """ find clients route """

    message = {}
    response = flask_adapter(request=request, api_route=find_client_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "clients",
                    "id": element.id,
                    "attributest": {
                        "name": element.name,
                    },
                    "relationships": {
                        "owner": {"type": "users", "id": element.user_id}
                    },
                }
            )

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/users", methods=["GET"])
def finder_users():
    """ find users route """

    message = {}
    response = flask_adapter(request=request, api_route=find_user_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "users",
                    "id": element.id,
                    "attributest": {"name": element.name},
                }
            )

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )