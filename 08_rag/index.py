from langchain_community.document_loaders import PyPDFLoader  # For loading PDF documents
from langchain_text_splitters import RecursiveCharacterTextSplitter  # For splitting text into manageable chunks
from langchain_openai import OpenAIEmbeddings  # For generating vector embeddings using OpenAI models
from langchain_qdrant import QdrantVectorStore  # For storing and searching embeddings in Qdrant vector database
from dotenv import load_dotenv  # For loading environment variables from a .env file

load_dotenv()  # Loads environment variables (like API keys) from .env file into the environment

from pathlib import Path  # For handling file paths in a platform-independent way

# Step 1: Load the PDF file using PyPDFLoader
pdf_path = Path(__file__).parent / "Nodejs.pdf"  # Get the path to the PDF file in the current folder
loader = PyPDFLoader(file_path=pdf_path)  # Initialize the PDF loader with the file path

docs = loader.load()  # Load the PDF and split it into a list of document objects (one per page or section)

# Step 2: Split the loaded documents into smaller chunks for better processing
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)  # Define chunk size and overlap
chunks = text_splitter.split_documents(documents=docs)  # Split the documents into chunks

# Step 3: Generate vector embeddings for each chunk using OpenAI's embedding model
embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-large"  # Specify the OpenAI embedding model to use
)

# Step 4: Store the embeddings in a Qdrant vector database for efficient similarity search
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,  # The list of document chunks
    embedding=embeddings_model,  # The embedding model to use
    url="http://localhost:6333",  # URL of the local Qdrant instance
    collection_name="nodejs_docs"  # Name of the collection in Qdrant
)

print("Vector store created successfully!")  # Confirmation message



