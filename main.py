# main.py
import os
from dotenv import load_dotenv
import openai

# Load local .env if it exists (for local testing)
load_dotenv()  # reads .env in the project root

# Get OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY as a secret or in a .env file.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# Example: simple ChatGPT query
try:
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant helping analyze exoplanet data."},
            {"role": "user", "content": "Which exoplanets are most likely habitable based on temperature and radius?"}
        ]
    )

    print("AI Response:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"Error communicating with OpenAI API: {e}")
