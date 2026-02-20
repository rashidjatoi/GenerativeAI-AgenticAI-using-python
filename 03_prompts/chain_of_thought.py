
# -------------------------------------------------------------
# Chain-of-Thought Prompt Example (with detailed comments)
# -------------------------------------------------------------
# This script demonstrates chain-of-thought prompting, where the AI assistant
# reasons step-by-step through a problem using START, PLAN, and OUTPUT steps.
# The assistant always responds in a strict JSON format for easy parsing.
# -------------------------------------------------------------

# Import required libraries
from dotenv import load_dotenv  # For loading environment variables
from openai import OpenAI       # For OpenAI API calls
import json                    # For parsing JSON responses

# Load environment variables (e.g., API keys) from .env file
load_dotenv()

# Create an authenticated OpenAI client
client = OpenAI()

# Define the system prompt with instructions and examples
# The prompt explains the chain-of-thought process and enforces JSON output
SYSTEM_PROMPT = """
    🤖 You're an expert AI assistant in resolving user queries using chain of thought! You work on START, PLAN, OUTPUT format.
    📝 You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    ✅ Once you think PLAN has been done, finally you can give an OUTPUT.

    📋 Rules:
    - Strictly follow the JSON output format mentioned below.
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), then PLAN (can be multiple steps), and then OUTPUT (which can be displayed to the user).
    
    🗂️ OUTPUT JSON FORMAT:
    {
     'step': 'START' or 'PLAN' or 'OUTPUT',
     "content" : "string"
    }

    💡 Example 1:
    Q: Hey, can you solve 2 + 3 * 5 for me?
    A: {"step": "START", "content": "Hey, can you solve 2 + 3 * 5 for me?"}
    A: {"step": "PLAN", "content": "Seems like user is interested in solving a mathematical expression. 🧮"}
    A: {"step": "PLAN", "content": "To solve the expression 2 + 3 * 5, we need to follow the order of operations (PEMDAS/BODMAS). First, we will calculate the multiplication part (3 * 5) and then add the result to 2."}
    A: {"step": "OUTPUT", "content": "The result of 2 + 3 * 5 is 17. 🎉"}

"""

# Initialize the message history with the system prompt
message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

# Get user input for the query
user_query = input("💬 Enter your query: ")

# Add the user's question to the message history
message_history.append({"role": "user", "content": user_query})

# Main loop: interact with the assistant until the OUTPUT step is reached
while True:
    # Send the conversation history to the OpenAI model
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},  # Enforce JSON output
        messages=message_history,
    )

    # Get the assistant's reply (should be a JSON string)
    assistant_reply = response.choices[0].message.content
    print("🤖 Assistant reply:", assistant_reply)

    try:
        # Parse the assistant's reply as JSON
        assistant_reply_json = json.loads(assistant_reply)
        # Add the assistant's reply to the message history
        message_history.append({"role": "assistant", "content": assistant_reply})
        # If the step is OUTPUT, end the loop
        if assistant_reply_json.get("step") == "OUTPUT":
            break
    except json.JSONDecodeError:
        # Handle parsing errors
        print("❌ Failed to parse assistant reply as JSON. Please check the format.")
        break

# End of script: the assistant's reply is always a JSON string for easy parsing and learning.
