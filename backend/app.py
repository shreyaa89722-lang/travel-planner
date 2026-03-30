from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ===== PLACES ROUTE =====
@app.route('/places', methods=['GET'])
def get_places():
    places = [
        {"name": "Goa Beach", "location": "Goa", "rating": 4.8, "category": "beach"},
        {"name": "Taj Mahal", "location": "Agra", "rating": 4.9, "category": "heritage"},
        {"name": "Munnar", "location": "Kerala", "rating": 4.7, "category": "nature"},
        {"name": "Jaipur", "location": "Rajasthan", "rating": 4.6, "category": "city"},
        {"name": "Manali", "location": "Himachal Pradesh", "rating": 4.7, "category": "mountain"},
    ]
    return jsonify({"success": True, "places": places})

# ===== BUDGET ROUTE =====
@app.route('/budget', methods=['POST'])
def save_budget():
    data = request.get_json()
    destination = data.get('destination')
    days = data.get('days')
    total = data.get('total')
    print(f"Budget saved: {destination} - {days} days - RS {total}")
    return jsonify({"success": True, "message": "Budget saved!"})

# ===== SUGGESTIONS ROUTE =====
@app.route('/suggestions', methods=['POST'])
def save_suggestion():
    data = request.get_json()
    name = data.get('name')
    suggestion = data.get('suggestion')
    print(f"Suggestion from {name}: {suggestion}")
    return jsonify({"success": True, "message": "Suggestion received!"})

# ===== TEST ROUTE =====
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Xplor Backend is running! 🚀"})

if __name__ == '__main__':
    app.run(debug=True)