import pytest

from pytestml.pytestcode.calculator import Calculator

class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(1000,1000,2000)])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect