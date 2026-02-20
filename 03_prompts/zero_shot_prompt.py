
# Zero-shot prompting: Giving instructions directly to the model without providing any examples.
# This script demonstrates how to use a zero-shot prompt with OpenAI's API.

# Import the OpenAI client class to make API requests to the OpenAI models.
from openai import OpenAI
# Import load_dotenv to load environment variables (like API keys) from a .env file.
from dotenv import load_dotenv

# Load environment variables from a .env file into the system environment.
# This is useful for keeping sensitive information (like API keys) out of your codebase.
load_dotenv()

# Create an authenticated OpenAI client using the API key from environment variables.
# The client will use the OPENAI_API_KEY variable loaded above.
client = OpenAI()

# Define the system prompt that sets the assistant's behavior.
# In zero-shot prompting, you give direct instructions to the model about how it should behave.
# Here, we instruct the model to only answer coding-related questions, introduce itself as 'alexa',
# and politely refuse to answer anything else.
SYSTEM_PROMPT = (
    "You should only answer coding-related questions. "
    "Do not answer anything else. Your name is Alexa. "
    "If the user asks something other than coding, just say 'Sorry.'"
)

# Prepare the chat completion request to the model.
# The 'messages' parameter is a list of message objects that define the conversation so far.
# The first message is a 'system' message that sets the assistant's rules and persona.
# The second message is a 'user' message containing the user's question.
response = client.chat.completions.create(
    model="gpt-4o",  # Specify the model to use (e.g., gpt-4o, gpt-3.5-turbo, etc.)
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},  # System prompt for assistant behavior
        {"role": "user", "content": "tell me about Agentic AI"}  # User's question
    ]
)

# Extract and print the assistant's reply from the response object.
# The response.choices list contains possible completions; we use the first one.
print(response.choices[0].message.content)
