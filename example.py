from pipe_function import pipe

# Example inputs
input1 = "Hello"
input2 = "World"

# Process the inputs with concatenation
combined = pipe(
    input1, input2,
    description="Concatenates two strings with a space between them"
)

# Print results
print(f"Input 1: {input1}")
print(f"Input 2: {input2}")
print(f"Combined: {combined}")

# Example input text
input_text = "This is a simple example text with seven words"

# Process the text with word count
num_words = pipe(
    input_text,
    description="Counts the number of words in a text"
)

# Print results
print(f"Input text: {input_text}")
print(f"Number of words: {num_words}")

# New examples without descriptions
text1 = "First example text"
text2 = "Second example text"

# Concatenation without description
combined_texts = pipe(text1, text2)

# Word count without description
word_count = pipe("This text has exactly five words")

# Print new results
print("\nExamples without descriptions:")
print(f"Combined texts: {combined_texts}")
print(f"Word count: {word_count}")



third_word = pipe("abc def ghi jkl")
print("third_word:", third_word)


