import pytest

class TestCal:
    # 测试add函数
    @pytest.mark.run(order=1)
    def test_add(self, get_cal, get_add_datas):
        result = None
        try:
            result = get_cal.add(get_add_datas[0], get_add_datas[1])
            if isinstance(result, float):
                result = round(result,2)
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]

    # 测试div函数
    @pytest.mark.run(order=4)
    def test_div(self, get_cal, get_div_datas):
        result = None
        try:
            result = get_cal.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_div_datas[2]

    # 测试sub函数
    @pytest.mark.run(order=2)
    def test_sub(self, get_cal, get_sub_datas):
        result = None
        try:
            result = get_cal.sub(get_sub_datas[0], get_sub_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_sub_datas[2]

    # 测试mul函数
    @pytest.mark.run(order=3)
    def test_mul(self, get_cal, get_mul_datas):
        result = None
        try:
            result = get_cal.mul(get_mul_datas[0], get_mul_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_mul_datas[2]

