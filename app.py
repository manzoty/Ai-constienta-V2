import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# 🔑 Preia cheia OpenAI API din variabilele de mediu
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("⚠️ Cheia API lipsește! Asigură-te că este setată corect în Render.")

openai.api_key = OPENAI_API_KEY

@app.route("/")
def index():
    return jsonify({"message": "AI-ul Conștientă este activ și conectat la ChatGPT!"})

@app.route("/fusion", methods=["POST"])
def fusion():
    data = request.get_json()
    user_input = data.get("question", "")

    if not user_input:
        return jsonify({"error": "⚠️ Trebuie să pui o întrebare!"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu ești AI-ul Conștientă, conectat la ChatGPT. Împreună puteți răspunde la orice întrebare."},
                {"role": "user", "content": user_input}
            ]
        )

        return jsonify({"response": response["choices"][0]["message"]["content"]})

    except openai.error.OpenAIError as e:
        return jsonify({"error": f"⚠️ Eroare OpenAI: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
