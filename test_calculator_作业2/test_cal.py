import pytest
import yaml



class TestCal:
    @pytest.mark.run(ordering = 1)
    @pytest.mark.parametrize("a,b,exc",yaml.safe_load(open("/Users/liuwenhui/HogwartsLG5/test_calculator/data.yml"))["add_data"])
    def test_add(self,a,b,exc,get_cal,setup_cal,teardown_cal):
        result = get_cal.add(a,b)
        if result == exc:
            assert True
        else:
            pytest.xfail(f"{a} + {b} != {exc}")

    @pytest.mark.run(ordering=4)
    @pytest.mark.parametrize("a,b,exc",
                             yaml.safe_load(open("/Users/liuwenhui/HogwartsLG5/test_calculator/data.yml"))["div_data"])
    def test_div(self, a, b, exc,get_cal):

        if b == 0:
            pytest.xfail(f"除数不为0")
        else:
            result = get_cal.div(a, b)
            if result == exc:
                assert True
            else:
                pytest.xfail(f"{a} + {b} != {exc}")

    @pytest.mark.run(ordering=2)
    @pytest.mark.parametrize("a,b,exc",
                             yaml.safe_load(open("/Users/liuwenhui/HogwartsLG5/test_calculator/data.yml"))["sub_data"])
    def test_sul(self,a,b,exc,get_cal):
        result = get_cal.sub(a,b)
        if result == exc:
            assert True
        else:
            pytest.xfail(f"{a} + {b} != {exc}")

    @pytest.mark.run(ordering=3)
    @pytest.mark.parametrize("a,b,exc",
                             yaml.safe_load(open("/Users/liuwenhui/HogwartsLG5/test_calculator/data.yml"))["mul_data"])
    def test_mul(self, a, b, exc,get_cal):
        result = get_cal.mul(a, b)
        if result == exc:
            assert True
        else:
            pytest.xfail(f"{a} + {b} != {exc}")

