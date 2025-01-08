import pytest
from module_factory import ModuleFactory

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
