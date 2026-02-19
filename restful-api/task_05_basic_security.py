#!/usr/bin/python3

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_required, JWTManager)

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

app.config["JWT_SECRET_KEY"] = "secret-key"

users = {
         "user1": {"username": "user1",
                   "password": generate_password_hash("password"),
                   "role": "user"},
         "admin1": {"username": "admin1",
                    "password": generate_password_hash("password"),
                    "role": "admin"}
}


@app.route("/basic-protected")
def basic_protected():
    return jsonify("Basic Auth: Access Granted")


@auth.verify_password
def verify_password(username, password):
    if (username in users and
       check_password_hash(users.get(username), password)):
        return username


@app.route("/login", methods=["POST"])
@auth.login_required
def login():
    data = request.get_json()
    username = request.json.get("username")
    password = request.json.get("password")
    if not request.is_json:
        return jsonify({"error: Invalid JSON"}), 400
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"Username and password required"}), 400
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"Invalid credentials"}), 401


@app.route("/jwt-required", methods=["GET"])
@jwt_required()
def jwt_required():
    return jsonify("JWT Auth: Access Granted"), 200


def is_admin():
    if not admin:
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"Admin Access: Granted"}), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
