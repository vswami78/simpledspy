from pipe_function import pipe

# Example input text
input_text = "This is a simple example text with seven words"

# Process the text
num_words = pipe(input_text, outputs=["num_words"])

# Print results
print(f"Input text: {input_text}")
print(f"Number of words: {num_words[0]}")
