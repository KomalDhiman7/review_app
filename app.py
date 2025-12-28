from flask import Flask, request, jsonify
from routes.auth_routes import auth_bp
from routes.review_routes import review_bp
from models.user_model import get_user_by_token
from routes.search_routes import search_bp
from routes.place_details_routes import place_details_bp


app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(review_bp)
app.register_blueprint(search_bp)
app.register_blueprint(place_details_bp)

def authenticate():
    """
    Checks Authorization header for valid token.
    """
    # token = request.headers.get("Authorization")
    # if not token:
    #     return None
    # return get_user_by_token(token)

    
    token = request.headers.get("Authorization")
    print("DEBUG TOKEN:", token)

    if not token:
        return None

    user = get_user_by_token(token)
    print("DEBUG USER:", user)

    return user


@app.before_request
def require_login():
    """
    Global auth enforcement.
    Allow registration without authentication.
    All other routes require a valid token.
    """

    # # Allow user registration endpoint
    if request.path.startswith("/register"):
        return


    # Allow ping
    if request.path == "/ping":
        return

    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Authentication required"}), 401

    user = get_user_by_token(token)
    if not user:
        return jsonify({"error": "Authentication required"}), 401


@app.route("/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(debug=True)




