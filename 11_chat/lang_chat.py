from typing_extensions import TypedDict  
from dotenv import load_dotenv  # To load environment variables from a .env file
from langgraph.graph import StateGraph, add_messages, START, END  # Core classes/functions for state-based graphs
from typing import Annotated  
from langchain_openai import ChatOpenAI  # LLM wrapper for OpenAI models

# Load environment variables (e.g., API keys) from a .env file
load_dotenv()

# Initialize the language model (GPT-4o variant) with a temperature for randomness
llm = ChatOpenAI(model="gpt-4o", temperature=0.9)

# Define the structure of the state dictionary used in the graph
# TypedDict allows us to specify what keys are expected in the dictionary
class State(TypedDict):
    # 'messages' is a list that will be used to store conversation messages
    # Annotated with 'add_messages' so that langgraph can handle message updates automatically
    messages: Annotated[list, add_messages]

# Function that interacts with the LLM
def chatbot(state: State):
    # Get messages from the state and send them to the LLM
    response = llm.invoke(state.get("messages"))
    # Return a new state containing the LLM's response
    return { "messages": [response] }

# Another example node in the graph
def samplenode(state: State):
    # Print current state for debugging
    print("\n\nInside samplenode node", state)
    # Return a state with a new message appended
    return { "messages": ["Sample Message Appended"] }

# Initialize a state graph using the State TypedDict
graph_builder = StateGraph(State)

# Add nodes to the graph (functions that will be executed in order)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

# Define edges (connections) between nodes
# START is a special node indicating the beginning of the graph
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
# END is a special node indicating the end of the graph
graph_builder.add_edge("samplenode", END)

# Compile the graph (prepare it for execution)
graph = graph_builder.compile()

# Execute the graph starting with an initial state
updated_state = graph.invoke(State({"messages": ["What is my name?"]}))

# Print the final state after running through all nodes
print("\n\nupdated_state", updated_state)