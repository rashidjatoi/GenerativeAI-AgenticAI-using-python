# Import the tiktoken library to convert text into tokens used by OpenAI models.
import tiktoken

# Create an encoder object that matches token rules for the gpt-4o model.
enc  = tiktoken.encoding_for_model("gpt-4o")

# Define the sample input text that we want to tokenize.
text = "Hello, how are you doing today? I hope you're having a great day!"

# Convert the text string into a list of token IDs.
tokens = enc.encode(text)

# Print the token IDs so we can see how text is split internally.
print("Tokens:", tokens)
# Print how many tokens are present in the tokenized output.
print("Number of tokens:", len(tokens))



# Decode the token IDs back to text and print the result to verify round-trip conversion.
print("\nDecoded text:", enc.decode(tokens))
