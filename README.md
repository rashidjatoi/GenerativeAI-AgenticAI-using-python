# Generative & Agentic AI using Python

This repository contains practical examples, scripts, and best practices for building modern AI applications using Python, OpenAI, Gemini, and related tools. It covers prompt engineering, agentic AI, retrieval-augmented generation (RAG), vector databases, and advanced transformer concepts.

## Directory Structure
- `01_tokenization/` — Tokenization basics and code examples
- `02_openai_hello/` — OpenAI and Gemini API usage, image generation, strict-topic assistants
- `03_prompts/` — Prompt engineering: zero-shot, one-shot, few-shot, chain-of-thought, JSON output
- `ATTENTIONS ALL YOU NEED` — Attention mechanisms and advanced AI concepts

## Key Concepts
- **Tokenization:** How text is split into tokens for model input
- **Basic AI Calls:** Making API requests to OpenAI and Gemini models
- **Prompt Engineering:** Zero-shot, one-shot, few-shot, chain-of-thought, and structured prompts
- **Agents:** Building agentic AI that can reason and act
- **RAG (Retrieval-Augmented Generation):** Combining search and generation for better answers
- **Vector DBs:** Using vector databases for semantic search and retrieval
- **Scalable AI Apps:** Designing AI applications for scalability and robustness
- **Vector Embedding:** Representing text and data as vectors for similarity search
- **Positional Encoding:** Encoding position information for transformer models
- **Self-Attention Mechanism:** Understanding how transformers focus on relevant parts of input
- **Zapier Automation:** Learned how Zapier works, how to connect apps and automate workflows, and created some flows for integrating AI outputs with other tools.

- **Zero-shot Prompt:** Direct instructions, no examples
- **One-shot Prompt:** One example provided
- **Few-shot Prompt:** Multiple examples provided
- **Chain-of-Thought Prompt:** Model is guided to reason step-by-step
- **Strict Topic Assistant:** AI answers only questions related to a specific topic
- **JSON Output Prompt:** Enforcing structured output for easy parsing

- **Persona Prompt:** The AI assistant takes on a specific persona (e.g., Rashid Ali) and answers as that character, demonstrating how to guide model behavior and style.

## Coding Practices
- Use `.env` files for API keys and secrets (never commit `.env` to git)
- Modularize code for clarity and reuse
- Add detailed comments for each script
- Use Python virtual environments for dependency management

## How to Run
1. Install dependencies:
   ```bash
   pip install openai python-dotenv
   ```
2. Add your API keys to `.env` (do not commit this file):
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   HUGGINGFACE_TOKEN=your_huggingface_token_here
   ```
3. Run any script, e.g.:
   ```bash
   python 03_prompts/zero_shot_prompt.py
   ```

## Security
- **Never commit your `.env` file or secrets to git.**
- `.env` is excluded via `.gitignore`.
- If secrets are accidentally committed, remove them from git history (see [GitHub guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)).

