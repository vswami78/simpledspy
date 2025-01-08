from pipe_function import pipe
from module_factory import ModuleFactory

# Create concatenation module
module_factory = ModuleFactory()
concatenator = module_factory.create_module(
    inputs=["text1", "text2"],
    outputs=["combined_text"],
    description="Concatenates two text inputs"
)

# Example inputs
input1 = "Hello"
input2 = "World"

# Process the inputs
combined = pipe(input1, input2, modules=[concatenator])

# Print results
print(f"Input 1: {input1}")
print(f"Input 2: {input2}")
print(f"Combined: {combined[0]}")

# Create word counter module
word_counter = module_factory.create_module(
    inputs=["text"],
    outputs=["num_words"],
    description="Counts number of words in text"
)

# Example input text
input_text = "This is a simple example text with seven words"

# Process the text
num_words = pipe(input_text, modules=[word_counter])

# Print results
print(f"Input text: {input_text}")
print(f"Number of words: {num_words[0]}")
