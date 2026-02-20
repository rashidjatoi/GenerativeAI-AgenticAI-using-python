

# -------------------------------------------------------------
# Few-Shot Prompt Example (with detailed comments)
# -------------------------------------------------------------
# This script demonstrates few-shot prompting, where the AI assistant
# is guided by multiple examples in the prompt. The assistant is instructed
# to answer only coding-related questions and refuse others politely.
# -------------------------------------------------------------



# Import the OpenAI client class to make API requests to the OpenAI models.
from openai import OpenAI
# Import load_dotenv to load environment variables (like API keys) from a .env file.
from dotenv import load_dotenv



# Load environment variables from a .env file into the system environment.
# This is useful for keeping sensitive information (like API keys) out of your codebase.
load_dotenv()




# Create an authenticated OpenAI client using the API key from environment variables.
client = OpenAI()



def add(a, b):
    return a + b

# Define the system prompt that sets the assistant's behavior and provides examples.
# In few-shot prompting, you give the model several Q&A examples to guide its responses.
# Here, we instruct the model to only answer coding-related questions, introduce itself as 'Alexa',
# and politely refuse to answer anything else. The prompt includes two example Q&A pairs:
#   - One off-topic question (math), which the assistant refuses.
#   - One on-topic question (Python code), which the assistant answers with code.
SYSTEM_PROMPT =  """You should only answer coding-related questions. 
Do not answer anything else. Your name is Alexa. 
If the user asks something other than coding, just say 'Sorry.'

Examples:
Q: can you explain the a + b whole square?
A: sorry, I can only answer coding related questions.

Q: hey, write a code in python for adding two numbers?
A: sure, here is a code in python for adding two numbers:
def add(a, b):
    return a + b
"""



# Prepare the chat completion request to the model.
# The 'messages' parameter is a list of message objects that define the conversation so far.
# The first message is a 'system' message that sets the assistant's rules, persona, and provides examples (few-shot).
# The second message is a 'user' message containing the user's question.
response = client.chat.completions.create(
    model="gpt-4o",  # Specify the model to use (e.g., gpt-4o, gpt-3.5-turbo, etc.)
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},  # System prompt for assistant behavior and examples
        {"role": "user", "content": "tell me about Agentic AI"}  # User's question
    ]
)

# Extract and print the assistant's reply from the response object.
# The response.choices list contains possible completions; we use the first one.
print(response.choices[0].message.content)
    model="gpt-4o",  # Specify the model to use (e.g., gpt-4o, gpt-3.5-turbo, etc.)
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},  # System prompt for assistant behavior and examples
        {"role": "user", "content": "write code to multiply two numbers"}  # User's question
    ]
)

# Extract and print the assistant's reply from the response object.
# The response.choices list contains possible completions; we use the first one.
print(response.choices[0].message.content)
