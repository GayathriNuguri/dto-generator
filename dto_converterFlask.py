from flask import Flask, request, jsonify
import google.generativeai as genai
from google.genai import types

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set")

genai.configure(api_key=GOOGLE_API_KEY)

model_config = types.GenerateContentConfig(
    temperature=0.0,
    top_p=0.95,
)

app = Flask(__name__)

def generate_dto(requirement: str):
    prompt = (
        f"Return only the Java class code block with no explanation, no comments, and "
        f"no extra methods other than fields, getters, setters, and constructors. "
        f"Create a DTO class with Requirement: {requirement}"
    )
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

@app.route('/generate-dto', methods=['POST'])
def generate_dto_api():
    try:
        data = request.get_json()
        requirement = data.get("requirement", "")
        dto_code = generate_dto(requirement)
        return jsonify({"dto": dto_code})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)