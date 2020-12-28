import pytest


def add(a,b):
    return a+b

class TestDemo:
    @pytest.mark.one
    def test_mark(self):
        assert  add(1,2) == 3