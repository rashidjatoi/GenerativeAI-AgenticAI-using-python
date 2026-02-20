# Import the OpenAI client class to make API requests.
from openai import OpenAI
# Import load_dotenv to read environment variables from a .env file.
from dotenv import load_dotenv

# Load values from .env into environment variables (for example, OPENAI_API_KEY).
load_dotenv()

# Create an authenticated OpenAI client using environment configuration.
client = OpenAI(
    api_key="AIzaSyC2IAlOXOD-UGJhtlPGN08d7uQ71nEPEDA",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)



# Send a chat completion request to the model with system and user messages.
response  = client.chat.completions.create(
    # Choose the model that should generate the reply.
    model="gemini-2.5-flash",
    # Provide the conversation messages in order: instruction first, then user input.
    messages=[
        # System message sets assistant behavior and style.
        {"role": "system", "content": "You are a helpful assistant."},
        # User message is the actual question/request to answer.
        {"role": "user", "content": "tell me about Agentic AI"}
    ]
)   


# Print only the assistant's generated text from the first response choice.
print(response.choices[0].message.content)