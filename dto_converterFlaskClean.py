from flask import Flask, request, jsonify
import google.generativeai as genai
from google.generativeai import GenerativeModel

# ✅ Configure API Key
GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"  # Replace with your actual key
genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)

def clean_dto_output(raw_output: str) -> str:
    """
    Cleans the Gemini output by removing ```java, backticks, and extra spaces/newlines.
    """
    cleaned = raw_output.replace("```java", "").replace("```", "").strip()
    return cleaned

def generate_dto(class_name: str, requirement: str) -> str:
    """
    Generates a Java DTO class based on requirement and custom class name.
    """
    prompt = (
        f"Return only the Java class code block with no explanation, no comments, and "
        f"no extra methods other than fields, getters, setters, and constructors. "
        f"Use class name: {class_name}. "
        f"Create a DTO class with Requirement: {requirement}"
    )
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return clean_dto_output(response.text)

@app.route('/generate-dto', methods=['POST'])
def generate_dto_api():
    try:
        data = request.get_json()
        requirement = data.get("requirement", "")
        class_name = data.get("className", "MyDTO")  # default name if not given

        dto_code = generate_dto(class_name, requirement)

        # ✅ Optional: Save to .java file
        file_path = f"{class_name}.java"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(dto_code)

        return jsonify({"dto": dto_code, "savedFile": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
