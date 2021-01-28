import pytest
import allure


@allure.title("计算器测试用例")
class TestCal:

    @pytest.mark.run(order=1)
    @allure.story("加法")
    def test_add(self, add_datas, get_cal):
        result = get_cal.add(add_datas[0], add_datas[1])
        try:
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            print(e)
        assert result == add_datas[2]


    @pytest.mark.run(order=4)
    @allure.story("除法")
    def test_div(self, div_datas, get_cal):
        result = get_cal.div(div_datas[0], div_datas[1])
        try:
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == div_datas[2]

    @pytest.mark.run(order=2)
    @allure.story("减法")
    def test_sub(self, sub_datas, get_cal):
        result = get_cal.sub(sub_datas[0], sub_datas[1])
        try:
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == sub_datas[2]

    @pytest.mark.run(order=3)
    @allure.story("乘法")
    def test_mul(self, mul_datas, get_cal):
        result = get_cal.mul(mul_datas[0], mul_datas[1])
        try:
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == mul_datas[2]


if __name__ == '__main__':
    pytest.main()