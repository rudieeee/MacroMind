from flask import Blueprint, request, jsonify
from services.ai_service import process_text
from services.nutrition_service import get_nutrition

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json

        # Validate input
        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        user_input = data.get("text")

        if not user_input.strip():
            return jsonify({"error": "Empty input"}), 400

        # Step 1: Process text (AI simulation)
        items = process_text(user_input)

        # Step 2: Get nutrition (fake data)
        nutrition = get_nutrition(items)

        return jsonify({
            "success": True,
            "input": user_input,
            "items": items,
            "nutrition": nutrition
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500