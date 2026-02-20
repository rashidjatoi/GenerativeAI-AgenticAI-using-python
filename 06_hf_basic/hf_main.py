# -------------------------------------------------------------
# Hugging Face Transformers Basic Example (with detailed comments)
# -------------------------------------------------------------
# This script demonstrates how to use Hugging Face's transformers pipeline
# for multimodal tasks (image and text input). It uses the Gemma model to
# answer a question about an image.
# -------------------------------------------------------------

# Import the pipeline function from Hugging Face transformers
from transformers import pipeline

# Create a pipeline for image-text-to-text tasks
# The model used is google/gemma-3-4b-it, which can process images and text
pipe = pipeline("image-text-to-text", model="google/gemma-3-4b-it")

# Define the input messages for the pipeline
# The user provides an image URL and a text question about the image
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]

# Run the pipeline with the input messages
# The output will be the model's answer to the user's question about the image
pipe(text=messages)