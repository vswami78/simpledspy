from pipe_function import pipe
from module_factory import ModuleFactory

# Configure language model (will be done automatically on first call if not configured)
pipe.configure_lm()

# Create word counter module
module_factory = ModuleFactory()
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
