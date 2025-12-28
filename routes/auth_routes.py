from flask import Blueprint, request, jsonify
import uuid
from models.user_model import create_user, get_user_by_phone

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Registers a new user.
    Input: name, phone
    Output: auth token
    """
    data = request.json
    name = data.get("name")
    phone = data.get("phone")

    if not name or not phone:
        return jsonify({"error": "Name and phone are required"}), 400

    # Check if phone already exists
    if get_user_by_phone(phone):
        return jsonify({"error": "Phone number already registered"}), 400

    token = str(uuid.uuid4())
    create_user(name, phone, token)

    return jsonify({
        "message": "User registered successfully",
        "token": token
    }), 201

    