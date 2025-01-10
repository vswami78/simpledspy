import pytest
from simpledspy import pipe

def test_multiple_outputs():
    """Test handling multiple return values"""
    text = "John Doe, 30 years old"
    
    name, age = pipe(text)
    assert name == "John Doe"
    assert age == "30"

