from google import genai
from dotenv import load_dotenv
import os


load_dotenv()
MODEL_NAME="models/gemini-3.5-flash"

def get_api_key():
    api_key=os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI API KEY not found")
    return api_key

def initialize_client():
    API_KEY=get_api_key()
    client=genai.Client(api_key=API_KEY)
    return client


def generate_response(prompt):
    client=initialize_client()

    response=client.models.generate_content(model=MODEL_NAME,contents=prompt)

    return response.text