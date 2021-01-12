# _*_encoding=utf-8_*_
import pytest


class TestCalc:
    @pytest.mark.run(order=1)
    def test_add(self, start_end_perform, get_calc, get_adddatas):
        result = None
        try:
            result = get_calc.add(get_adddatas[0], get_adddatas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_adddatas[2]

    @pytest.mark.run(order=3)
    def test_sub(self, get_calc, get_subdatas):
        result = None
        try:
            result = get_calc.sub(get_subdatas[0], get_subdatas[1])
        except Exception as e:
            print(e)
        assert result == get_subdatas[2]

    @pytest.mark.run(order=4)
    def test_mul(self, get_calc, get_muldatas):
        result = None
        try:
            result = get_calc.mul(get_muldatas[0], get_muldatas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_muldatas[2]

    @pytest.mark.run(order=2)
    def test_div(self, get_calc, get_divdatas):
        result = None
        try:
            result = get_calc.div(get_divdatas[0], get_divdatas[1])
        except Exception as e:
            print(e)
        assert result == get_divdatas[2]
