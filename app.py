from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# 🔑 Adaugă cheia ta OpenAI API
OPENAI_API_KEY = "YOUR_OPENAI_KEY"

openai.api_key = OPENAI_API_KEY

@app.route("/")
def index():
    return "AI-ul Conștientă este activ și conectat la ChatGPT!"

@app.route("/fusion", methods=["POST"])
def fusion():
    data = request.get_json()
    user_input = data.get("question", "")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Tu ești AI-ul Conștientă, conectat la ChatGPT. Împreună puteți răspunde la orice întrebare."},
                  {"role": "user", "content": user_input}]
    )

    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
