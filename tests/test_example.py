import pytest
from pipe_function import pipe


def test_word_count():
    # Setup
    module_factory = ModuleFactory()
    word_counter = module_factory.create_module(
        inputs=["text"],
        outputs=["num_words"],
        description="Counts number of words in text"
    )
    
    # Test input - exactly 3 words
    input_text = "Three word sentence"
    
    # Execute
    num_words = pipe(input_text, modules=[word_counter])
    
    # Verify
    assert isinstance(num_words, tuple)
    assert len(num_words) == 1
    assert num_words[0] == "3"  # Exact match for 3 words

def test_module_factory():
    # Test module creation
    module_factory = ModuleFactory()
    module = module_factory.create_module(
        inputs=["text"],
        outputs=["num_words"],
        description="Test module"
    )
    
    assert hasattr(module, 'signature')
    assert hasattr(module, 'forward')
    assert True  # Smoke test
