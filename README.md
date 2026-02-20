#######################################################################
# Generative & Agentic AI Coding Learnings
#
# This README is designed for learning purposes. It explains all the key
# concepts, coding techniques, prompt engineering strategies, and best
# practices covered in this workspace. Each section is commented for clarity.
#######################################################################

# -----------------------------
# Directory Structure
# -----------------------------
# - `01_tokenization/`: Contains scripts and explanations about tokenization,
#   which is the process of breaking text into tokens for model input.
# - `02_openai_hello/`: Demonstrates basic API calls to OpenAI and Gemini,
#   image generation, and strict-topic assistants.
# - `03_prompts/`: Focuses on prompt engineering, including zero-shot,
#   one-shot, few-shot, chain-of-thought, and JSON output prompts.
# - `ATTENTIONS ALL YOU NEED`: Covers attention mechanisms and advanced AI concepts.

# -----------------------------
# Key Concepts Learned
# -----------------------------
# - **Tokenization:** Essential for preparing text for AI models.
# - **Basic AI Calls:** How to interact with OpenAI and Gemini APIs.
# - **Prompt Engineering:** Crafting prompts for different learning modes.
# - **Agents:** Building agentic AI that can reason and act autonomously.
# - **RAG:** Retrieval-Augmented Generation, combining search and generation.
# - **Vector DBs:** Using vector databases for semantic search.
# - **Scalable AI Apps:** Designing robust, scalable AI applications.
# - **Vector Embedding:** Representing data as vectors for similarity search.
# - **Positional Encoding:** Used in transformers to encode sequence position.
# - **Self-Attention Mechanism:** Allows models to focus on relevant input parts.

# -----------------------------
# Prompt Engineering Examples
# -----------------------------
# - **Zero-shot Prompt:** Direct instructions, no examples.
# - **One-shot Prompt:** One example provided.
# - **Few-shot Prompt:** Multiple examples provided.
# - **Chain-of-Thought Prompt:** Guides the model to reason step-by-step.
# - **Strict Topic Assistant:** AI answers only questions related to a specific topic.
# - **JSON Output Prompt:** Enforces structured output for easy parsing.

# -----------------------------
# Coding Practices
# -----------------------------
# - Use `.env` files for API keys and secrets to keep credentials secure.
# - Modularize code for clarity and reuse.
# - Add detailed comments for each script to aid learning.
# - Use Python virtual environments for dependency management.

# -----------------------------
# How to Run
# -----------------------------
# 1. Install dependencies:
#    pip install openai python-dotenv
   ```
2. Add your API keys to `.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Run any script, e.g.:
   ```
   python 03_prompts/zero_shot_prompt.py
   ```

## Further Reading
- See `learings.txt` for a quick list of concepts
- Explore each directory for code examples and detailed scripts

## Author
GitHub Copilot (GPT-4.1)

---
Feel free to expand this README as you learn more or add new scripts!
