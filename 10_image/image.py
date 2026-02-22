from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()


response  = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role" : "user",
            "content" : [
                 {
                    "type": "text",
                    "text": "Generate the caption for this image in about 50 words."
                 },
                    {
                        "type": "image_url",
                        "image_url": {'url': "https://images.unsplash.com/photo-1536104968055-4d61aa56f46a?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"}
                    }
            ]
        }
    ]
    )

print(response)