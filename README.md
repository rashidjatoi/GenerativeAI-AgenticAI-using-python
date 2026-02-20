# Generative & Agentic AI using Python

This repository is a comprehensive collection of practical code, concepts, and workflows for building modern AI applications using Python. It covers everything from the basics of tokenization to advanced prompt engineering, agentic AI, automation, and integration with popular tools and platforms.

## Directory Structure
- `01_tokenization/` — Learn how text is broken down into tokens, why tokenization matters for LLMs, and see code examples for tokenizing text in Python.
- `02_openai_hello/` — Hands-on scripts for using OpenAI and Gemini APIs, including text and image generation, and building assistants that answer only on specific topics.
- `03_prompts/` — Deep dive into prompt engineering: zero-shot, one-shot, few-shot, chain-of-thought, persona, and JSON-structured prompts, with code and detailed comments.
- `04_prompt_serialization_styles/` — Examples of prompt serialization styles (Alpaca, ChatML, INST) for different LLMs.
- `ATTENTIONS ALL YOU NEED` — Theory and code for attention mechanisms, positional encoding, and transformer internals.

## What I Learned (Descriptive)

### Tokenization
Discovered how LLMs process text by splitting it into tokens. Learned about different tokenization strategies, why tokenization is crucial for model input, and how it affects prompt length and cost.

### Basic AI Calls
Gained hands-on experience making API requests to OpenAI, Gemini, and other LLM providers. Understood authentication, request/response structure, and how to handle outputs in Python.

### Prompt Engineering
Explored various prompt types:
- **Zero-shot:** Direct instructions to the model, no examples. Useful for simple tasks.
- **One-shot:** One example provided to guide the model.
- **Few-shot:** Multiple examples to help the model generalize and follow patterns.
- **Chain-of-Thought:** Prompting the model to reason step-by-step, improving accuracy for complex tasks.
- **Persona Prompt:** Setting a specific persona (e.g., Rashid Ali) so the AI answers in a consistent style or character.
- **Strict Topic Assistant:** Restricting the AI to only answer questions on a specific topic.
- **JSON Output Prompt:** Enforcing structured, machine-readable output for downstream automation.

### Agents
Learned about agentic AI—building systems that can reason, plan, and act autonomously. Explored how agents can use tools, call APIs, and chain multiple steps to solve real-world problems.

### RAG (Retrieval-Augmented Generation)
Studied how to combine LLMs with external knowledge sources (like vector databases) to answer questions with up-to-date or domain-specific information. Implemented simple RAG flows.

### Vector DBs & Embeddings
Learned how to represent text and data as high-dimensional vectors (embeddings) and use vector databases for semantic search, retrieval, and context injection into LLM prompts.

### Scalable AI Apps
Explored best practices for designing AI applications that are robust, modular, and scalable. Used environment variables, virtual environments, and modular code organization.

### Positional Encoding & Self-Attention
Understood how transformers encode the position of tokens and use self-attention to focus on relevant parts of the input, enabling powerful sequence modeling.

### Automation with Zapier
Learned how to use Zapier to connect different apps and automate workflows. Created flows that trigger on AI outputs, send notifications, or update other systems, making AI solutions more actionable.

### Ollama & Open Web UI
Set up and managed local LLMs using Ollama, including model installation, prompt testing, and integration with Python. Built a FastAPI server to expose Ollama's LLMs as web APIs, allowing easy integration with web apps and other services. Used Open Web UI to interact with LLMs in the browser, customize chat interfaces, and visually test prompt engineering. Integrated Ollama Docker container with Open Web UI Docker container for seamless browser-based LLM interaction.

### Prompt Serialization Styles
Explored different prompt serialization formats (Alpaca, ChatML, INST) to ensure compatibility with various LLMs and platforms. See `04_prompt_serialization_styles/prompt_styles.py` for detailed examples and comments.

### OpenAI Playground
Experimented with the OpenAI Playground to interactively test prompts, visualize model responses, and fine-tune prompt engineering before coding. This tool helped in rapid prototyping and understanding model behavior in a user-friendly web interface.

### Google Colab
Used Google Colab for running Python notebooks in the cloud, leveraging free GPU resources for model experimentation, data processing, and collaborative AI development. Integrated Colab with APIs and external datasets for end-to-end workflows.

### Weather Agent Project
Developed a conversational weather agent that uses chain-of-thought prompting and tool use. The agent can reason step-by-step, call external tools (like a weather API or shell commands), and return answers in a structured JSON format. Integrated OpenAI's API, Pydantic for output validation, and demonstrated how to build flexible, tool-using AI assistants. This project showcases advanced prompt engineering, tool-calling logic, and real-world API integration for practical AI workflows.

## Coding & Security Best Practices
- Use `.env` files for API keys and secrets (never commit `.env` to git)
- Modularize code for clarity and reuse
- Add detailed comments to all scripts for learning and collaboration
- Use Python virtual environments for dependency management
- If secrets are accidentally committed, remove them from git history ([GitHub guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository))

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

---
This repository is a living document of my AI learning journey. Feel free to explore, use, and expand on these examples!

