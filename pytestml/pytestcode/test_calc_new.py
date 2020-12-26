import pytest

@pytest.fixture(scope="class")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc

class TestCalc:

    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(1000,1000,2000)])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect