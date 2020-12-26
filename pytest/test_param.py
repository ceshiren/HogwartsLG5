import pytest

def add_function(a,b):
    return a+b
@pytest.mark.parametrize("a,b,expected",[(3,3,6),(-1,-2,-3),(1000,1000,2000)],ids=["int","minus","bigint"])
def test_add(a,b,expected):
    assert add_function(a,b) == expected