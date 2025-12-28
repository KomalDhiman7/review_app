from flask import Blueprint, request, jsonify
from models.place_model import (
    get_place_by_name_and_address,
    create_place
)
from models.review_model import (
    create_review,
    user_has_reviewed_place
)
from models.user_model import get_user_by_token

review_bp = Blueprint("reviews", __name__)

@review_bp.route("/reviews", methods=["POST"])
def add_review():
    """
    Add a review for a place.
    If the place does not exist, it is created.
    A user can review a place only once.
    """

    # Authentication

    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Authentication required"}), 401

    user = get_user_by_token(token)
    if not user:
        return jsonify({"error": "Invalid token"}), 401

    # Input validation
    data = request.json
    place_name = data.get("place_name")
    place_address = data.get("place_address")
    rating = data.get("rating")
    text = data.get("text", "")

    if not place_name or not place_address or not rating:
        return jsonify({"error": "Missing required fields"}), 400

    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    # place lookup
    place = get_place_by_name_and_address(place_name, place_address)

    # If place does not exist, create it
    if not place:
        create_place(place_name, place_address)
        place = get_place_by_name_and_address(place_name, place_address)

    # duplicate review check
    if user_has_reviewed_place(user["id"], place["id"]):
        return jsonify({"error": "User has already reviewed this place"}), 400

    # -create review
    create_review(
        rating=rating,
        text=text,
        user_id=user["id"],
        place_id=place["id"]
    )

    return jsonify({"message": "Review added successfully"}), 201
