from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# ✅ Supabase connection
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# ===== HOME =====
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Xplor Backend is running! 🚀"})

# ===== PLACES — load from Supabase =====
@app.route('/places', methods=['GET'])
def get_places():
    try:
        response = supabase.table("places").select("*").execute()
        return jsonify({"success": True, "places": response.data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ===== BUDGET — save to Supabase =====
@app.route('/budget', methods=['POST'])
def save_budget():
    try:
        data = request.get_json()
        supabase.table("budgets").insert({
            "destination": data.get("destination"),
            "days": data.get("days"),
            "people": data.get("people"),
            "total": data.get("total")
        }).execute()
        return jsonify({"success": True, "message": "Budget saved!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ===== SUGGESTIONS — save to Supabase =====
@app.route('/suggestions', methods=['POST'])
def save_suggestion():
    try:
        data = request.get_json()
        supabase.table("suggestions").insert({
            "name": data.get("name"),
            "suggestion": data.get("suggestion")
        }).execute()
        return jsonify({"success": True, "message": "Suggestion saved!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
