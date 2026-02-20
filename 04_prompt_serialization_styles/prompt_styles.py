
# -------------------------------------------------------------
# Prompt Serialization Styles (with detailed comments)
# -------------------------------------------------------------
# This file demonstrates different prompt serialization styles used in
# instruction-tuned and chat-based large language models (LLMs).
# Understanding these formats helps you design prompts compatible with
# various open-source and commercial models.
# -------------------------------------------------------------

# 1. Alpaca Prompt Template (Instruction Tuning)
# -------------------------------------------------------------
# Used for models like Alpaca and other instruction-tuned LLMs.
# The prompt is divided into three sections:
#   - instructions: The system prompt or task description
#   - input: The user's query or input
#   - Response: Where the model's answer should go
# Example:
#   ### instructions <SYSTEM_PROMPT>\n
#   ### input <USER_QUERY>\n
#   ### Response:\n


# 2. ChatML Schema (OpenAI’s Structured Prompt Format)
# -------------------------------------------------------------
# ChatML is a structured format for designing prompts that guide AI assistants
# in generating responses. It uses a clear schema to define the roles of different
# messages in a conversation, making it easier to create complex interactions.
# Each message is represented as a dictionary with two keys: 'role' and 'content'.
# Roles can be 'system', 'user', or 'assistant'.
# Example:
#   {'role': 'system', 'content': 'You are a helpful assistant.'}
#   {'role': 'user', 'content': 'What is the capital of France?'}
#   {'role': 'assistant', 'content': 'The capital of France is Paris.'}


# 3. INST Format (LLaMA-2 Instruction Specification)
# -------------------------------------------------------------
# The INST format is used for instruction tuning, especially with models like LLaMA-2.
# It wraps the user query (and optionally the system prompt) in [INST] ... [/INST] tags.
# The model is expected to generate a response based on the instructions provided.
# Example:
#   [INST] What is the time now? [/INST]