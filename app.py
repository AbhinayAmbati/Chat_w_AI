from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Set your Gemini API key here
GEMINI_API_KEY = "your gemini api key here"
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json["message"]

        # Call Gemini API
        response = model.generate_content(user_message)

        # Extract the AI's response
        ai_message = response.text
        return jsonify({"message": ai_message})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)