from pipe_function import pipe

# Example inputs
input1 = "Hello"
input2 = "World"

# Process the inputs
combined = pipe(input1, input2)

# Print results
print(f"Input 1: {input1}")
print(f"Input 2: {input2}")
print(f"Combined: {combined[0]}")

# Example input text
input_text = "This is a simple example text with seven words"

# Process the text
num_words = pipe(input_text)

# Print results
print(f"Input text: {input_text}")
print(f"Number of words: {num_words[0]}")
