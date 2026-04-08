from flask import Flask, request, jsonify
from flask_cors import CORS
from agent.llm_agent import get_llm_response

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    user_input = data.get("input")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        result = get_llm_response(user_input)
        return jsonify(result)
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
#  ---- To Run this file  ---- :    python -m backend.app