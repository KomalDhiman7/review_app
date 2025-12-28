from flask import Blueprint, request, jsonify
from models.user_model import get_user_by_token
from models.search_model import search_places

search_bp = Blueprint("search", __name__)

@search_bp.route("/search", methods=["GET"])
def search():
    # ---- AUTH ----
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Authentication required"}), 401

    user = get_user_by_token(token)
    if not user:
        return jsonify({"error": "Authentication required"}), 401

    # ---- QUERY PARAMS ----
    name = request.args.get("name", "").strip()
    min_rating = request.args.get("min_rating", 0)

    try:
        min_rating = float(min_rating)
    except ValueError:
        return jsonify({"error": "min_rating must be a number"}), 400

    if not name:
        return jsonify({"error": "Search name is required"}), 400

    results = search_places(name, min_rating)

    return jsonify(results), 200
