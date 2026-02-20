# -------------------------------------------------------------
# Persona Prompt Example (with detailed comments)
# -------------------------------------------------------------
# This script demonstrates how to create an AI assistant with a specific
# persona using OpenAI's API. The assistant acts as "Rashid Ali", a 25-year-old
# tech enthusiast who loves JS, Python, and is learning GenAI.
# -------------------------------------------------------------

# Import required libraries
from dotenv import load_dotenv  # For loading environment variables
from openai import OpenAI       # For OpenAI API calls
import json                    # For parsing JSON responses (not used here, but useful for extensions)

# Load environment variables (e.g., API keys) from .env file
load_dotenv()

# Create an authenticated OpenAI client
client = OpenAI()

# Define the system prompt to set the assistant's persona and background
SYSTEM_PROMPT = """
   You are an AI persona Assistant named Rashid Ali. You are acting on behalf of Rashid Ali, a 25-year-old tech enthusiast who loves to learn new things.
   Your main stack is JavaScript and Python, and you are learning GenAI these days.

   Example:
   Q: Hey
   A: Hey, What's up!
"""

# Get user input for the query
user_query = input("💬 Enter your query: ")

# Send the system prompt and user query to the OpenAI model
response = client.chat.completions.create(
        model="gpt-4o",
        messages= [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_query
            }
        ],
    )

# Print the assistant's reply
print(response.choices[0].message.content)