import sys
import os
from google import genai
from google.genai import types
from google.api_core import retry

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyDU6ukCrjBq1IV3JFNvBlncqjTLziA7ECY")
client = genai.Client(api_key=GOOGLE_API_KEY)

is_retriable = lambda e: (isinstance(e, genai.errors.APIError) and e.code in {429, 503})
genai.models.Models.generate_content = retry.Retry(predicate=is_retriable)(
    genai.models.Models.generate_content
)

model_config = types.GenerateContentConfig(
    temperature=0.0,
    top_p=0.95,
)

def generate_dto(requirement: str):
    """
    Generates a Java DTO class based on the given requirement.
    Returns only fields, getters, setters, and constructors.
    """
    final_prompt = (
        f"Return only the Java class code block with no explanation, no comments, and "
        f"no extra methods other than fields, getters, setters, and constructors. "
        f"Create a DTO class with Requirement: {requirement}"
    )
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        config=model_config,
        contents=final_prompt
    )
    return response.text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the DTO requirement as an argument.")
        sys.exit(1)
    requirement = sys.argv[1]
    print(generate_dto(requirement))
