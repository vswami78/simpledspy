from pipe_function import pipe

# Example inputs
input1 = "Hello"
input2 = "World"

def combine_strings(text1: str, text2: str) -> str:
    """Concatenates two strings with a space between them"""
    return f"{text1} {text2}"

# Process the inputs with concatenation
concatenated = pipe(combine_strings, input1, input2)

# Print results
print(f"Input 1: {input1}")
print(f"Input 2: {input2}")
print(f"Combined: {concatenated[0]}")

# Example input text
input_text = "This is a simple example text with seven words"

def count_words(text: str) -> int:
    """Counts the number of words in a text"""
    return len(text.split())

# Process the text with word count
num_words = pipe(count_words, input_text)

# Print results
print(f"Input text: {input_text}")
print(f"Number of words: {num_words[0]}")
