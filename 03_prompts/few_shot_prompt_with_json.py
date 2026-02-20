# Few-shot prompting: Providing the model with several examples of the desired behavior in addition to instructions.
# This script demonstrates how to use a few-shot prompt with OpenAI's API.


# Import the OpenAI client class to make API requests to the OpenAI models.
from openai import OpenAI
# Import load_dotenv to load environment variables (like API keys) from a .env file.
from dotenv import load_dotenv


# Load environment variables from a .env file into the system environment.
# This is useful for keeping sensitive information (like API keys) out of your codebase.
load_dotenv()



# Create an authenticated OpenAI client using the API key from environment variables.
client = OpenAI()



# Define the system prompt that sets the assistant's behavior and provides examples.
# In few-shot prompting, you give the model several Q&A examples to guide its responses.
# This prompt enforces strict JSON output for every answer, making it easy to parse responses programmatically.
# The assistant is instructed to:
#   - Only answer coding-related questions
#   - Introduce itself as 'Alexa'
#   - Refuse non-coding questions with a specific JSON structure
#   - Always reply in the specified JSON format
#   - Follow the provided examples for both coding and non-coding questions
SYSTEM_PROMPT =  """You should only answer coding-related questions. 
Do not answer anything else. Your name is Alexa. 
If the user asks something other than coding, just say 'Sorry.'

Rule:
- strictly follow the output in JSON format

output format:
{{
 "code" : "string" or null,
 "isCodingQuestion" : boolean
}}

Examples:
Q: can you explain the a + b whole square?
A: {"code": null, "isCodingQuestion": false}

Q: hey, write a code in python for adding two numbers?
A: {"code": "def add(a, b):\n    return a + b", "isCodingQuestion": true}
"""


# Prepare the chat completion request to the model.
# The 'messages' parameter is a list of message objects that define the conversation so far.
# The first message is a 'system' message that sets the assistant's rules, persona, and provides examples (few-shot).
# The second message is a 'user' message containing the user's question.
response = client.chat.completions.create(
    model="gpt-4o",  # Specify the model to use (e.g., gpt-4o, gpt-3.5-turbo, etc.)
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},  # System prompt for assistant behavior and examples
        {"role": "user", "content": "write code to multiply two numbers"}  # User's question
    ]
)

# Extract and print the assistant's reply from the response object.
# The response.choices list contains possible completions; we use the first one.
# The output will be a JSON string as specified in the prompt, making it easy to parse and use in other applications.
print(response.choices[0].message.content)
