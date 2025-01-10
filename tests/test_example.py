import pytest
from simpledspy import pipe

def test_second_word_extraction():
    """Test extracting second word from text"""
    list_jkl = "abc def ghi jkl iowe afj wej own iow jklwe"
    list_oqc = "oid iwfo fjs wjiof sfio we x dso weop vskl we"
    
    second_word_list_oqc = pipe(list_jkl, list_oqc)
    assert second_word_list_oqc == "iwfo"

