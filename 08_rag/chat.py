
from dotenv import load_dotenv  # For loading environment variables from a .env file
from langchain_openai import OpenAIEmbeddings  # For generating vector embeddings using OpenAI models
from langchain_qdrant import QdrantVectorStore  # For interacting with the Qdrant vector database
from openai import OpenAI  # For accessing OpenAI's chat models

# Load environment variables (like API keys) from .env file
load_dotenv() 

# Initialize the OpenAI client for chat completion
openai_client = OpenAI()

# Set up the embedding model to match the one used during indexing
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-large"  # Use the same embedding model as in index.py
)

# Connect to the existing Qdrant vector database collection
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",  # Qdrant instance URL
    collection_name="nodejs_docs",  # Name of the collection created during indexing
    embedding=embeddings_model,  # Embedding model for queries
)

# Prompt the user for a query
user_query = input("Enter your query: ")

# Search the vector database for the top 3 most relevant chunks to the user query
search_results = vector_db.similarity_search(query=user_query, k=3)

# Prepare the context from the search results to provide to the language model
context = "\n\n\n".join([
    f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
    for result in search_results
])

# System prompt to instruct the AI assistant on how to answer
SYSTEM_PROMPT = f"""
 You are a helpful AI Assistant who answers user queries based on the available context retrieved from a PDF file, including page contents and page number.

 You should only answer the user based on the following context and guide the user to open the right page number to know more. Also, explain the context of the question from the PDF that they are asking about.

 Context:
 {context}
"""

# Generate a response from the OpenAI chat model using the context and user query
response = openai_client.chat.completions.create(
    model="gpt-5",  # Specify the chat model to use
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ]
)

# Print the AI assistant's response
print(f"🤖: {response.choices[0].message.content}")