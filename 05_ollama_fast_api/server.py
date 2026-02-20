# -------------------------------------------------------------
# Ollama FastAPI Server Example (with detailed comments)
# -------------------------------------------------------------
# This script demonstrates how to build a simple FastAPI server that
# connects to a local Ollama LLM server and exposes a chat endpoint.
# You can use this to build web APIs for LLMs running locally.
# -------------------------------------------------------------

# Import FastAPI for building web APIs and Body for request parsing
from fastapi import FastAPI, Body
# Import Ollama client for interacting with local LLMs
from ollama import Client

# Initialize FastAPI app
app = FastAPI()

# Connect to the Ollama server (default URL is localhost:11434)
client = Client(
    host='http://localhost:11434'  # Default Ollama server URL
)

# Root endpoint for health check or basic info
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Chat endpoint: accepts a user message and returns LLM response
@app.post("/chat")
def Chat(
        message: str = Body(..., example="What is the capital of France?")
    ):
    # Send the user message to Ollama's chat API (using gemma:2b model)
    response = client.chat(model='gemma:2b', messages=[{"role": "user", "content": message}])
    # Return the LLM's response as JSON
    return {"response": response.message.content}
