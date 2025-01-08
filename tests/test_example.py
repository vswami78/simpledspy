import pytest
import dspy
from module_factory import ModuleFactory

@pytest.fixture(autouse=True)
def setup_dspy():
    """Configure DSPy with a test language model before each test"""
    # Use a simple test LM that just echoes inputs
    lm = dspy.HFClientTGI(model="meta-llama/Llama-2-7b-chat-hf", port=8080, url="http://localhost")
    dspy.settings.configure(lm=lm)

def test_module_creation():
    """Test basic module creation with inputs and outputs"""
    factory = ModuleFactory()
    module = factory.create_module(
        inputs=["text"],
        outputs=["length"],
        description="Test module that returns input length"
    )
    
    # Verify module has expected attributes
    assert hasattr(module, 'signature')
    assert hasattr(module, 'forward')
    
    # Test module with sample input
    result = module(text="hello world")
    assert hasattr(result, "length")  # Verify output field exists

def test_multiple_inputs_outputs():
    """Test module with multiple inputs and outputs"""
    factory = ModuleFactory()
    module = factory.create_module(
        inputs=["text1", "text2"],
        outputs=["combined", "length"],
        description="Combine two texts and return length"
    )
    
    # Test with multiple inputs
    result = module(text1="hello", text2="world")
    assert hasattr(result, "combined")
    assert hasattr(result, "length")
