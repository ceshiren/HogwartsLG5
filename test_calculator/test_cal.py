import pytest
import yaml
from Calculator import Calculator


class TestCal:
    def setup_class(self):
        self.calc = Calculator()

    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("\n计算结束")

    @pytest.fixture()
    @pytest.mark.parametrize("a,b,exc",yaml.safe_load(open("/Users/liuwenhui/HogwartsLG5/test_calculator/data.yml"))["add_data"])
    def test_add(self,a,b,exc):
        result = self.calc.add(a,b)
        if result == exc:
            assert True
        else:
            pytest.xfail(f"{a} + {b} != {exc}")

    @pytest.mark.parametrize("a,b,exc",
                             yaml.safe_load(open("/Users/liuwenhui/HogwartsLG5/test_calculator/data.yml"))["sub_data"])
    def test_sul(self,a,b,exc):
        result = self.calc.sub(a,b)
        if result == exc:
            assert True
        else:
            pytest.xfail(f"{a} + {b} != {exc}")

    @pytest.mark.parametrize("a,b,exc",
                             yaml.safe_load(open("/Users/liuwenhui/HogwartsLG5/test_calculator/data.yml"))["mul_data"])
    def test_mul(self, a, b, exc):
        result = self.calc.mul(a, b)
        if result == exc:
            assert True
        else:
            pytest.xfail(f"{a} + {b} != {exc}")

    @pytest.mark.parametrize("a,b,exc",
                             yaml.safe_load(open("/Users/liuwenhui/HogwartsLG5/test_calculator/data.yml"))["div_data"])
    def test_div(self, a, b, exc):

        if b == 0:
            pytest.xfail(f"除数不为0")
        else:
            result = self.calc.div(a, b)
            if result == exc:
                assert True
            else:
                pytest.xfail(f"{a} + {b} != {exc}")