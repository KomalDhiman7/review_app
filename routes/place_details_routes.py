from flask import Blueprint, request, jsonify
from models.user_model import get_user_by_token
from models.place_details_model import get_place_details

place_details_bp = Blueprint("place_details", __name__)

@place_details_bp.route("/places/<int:place_id>", methods=["GET"])
def place_details(place_id):
    # ---- AUTH ----
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Authentication required"}), 401

    user = get_user_by_token(token)
    if not user:
        return jsonify({"error": "Authentication required"}), 401

    result = get_place_details(place_id, user["id"])

    if not result:
        return jsonify({"error": "Place not found"}), 404

    return jsonify(result), 200
