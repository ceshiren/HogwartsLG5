from math import fabs

import pytest
import yaml

from test_pytest.pythoncode.calculator import Calculator


def read_datas():
    # 打开yml文件
    with open("./data.yml", mode='r', encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
        print(datas)
        # 获取文件的datas数据
        add_datas = datas["add_data"]
        sub_datas = datas["sub_data"]
        mul_datas = datas["mul_data"]
        div_datas = datas["div_data"]
        # 获取文件的myids文件
        return [add_datas, sub_datas, mul_datas, div_datas]


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def setup_method(self):
    print("开始计算")


def teardown_method():
    print("计算结束")


class TestCal:
    def setup_class(self):
        # 实例化类，生成类的参数
        self.cal = Calculator()

    @pytest.mark.parametrize("a,b,expect", read_datas()[0])
    def test_add(self, a, b, expect):
        if is_number(a) & is_number(b):
            result1 = self.cal.add(a, b)
            assert fabs(result1 - expect) < 0.0001

    @pytest.mark.parametrize("a,b,expect", read_datas()[1])
    def test_sub(self, a, b, expect):
        if is_number(a) & is_number(b):
            result2 = self.cal.sub(a, b)
            assert fabs(result2 - expect) < 0.0001

    @pytest.mark.parametrize("a,b,expect", read_datas()[2])
    def test_mul(self, a, b, expect):
        if is_number(a) & is_number(b):
            result3 = self.cal.mul(a, b)
            assert fabs(result3 - expect) < 0.0001

    @pytest.mark.parametrize("a,b,expect", read_datas()[3])
    def test_div(self, a, b, expect):
        if is_number(a) & is_number(b):
            if b != 0:
                result4 = self.cal.div(a, b)
                assert fabs(result4 - expect) < 0.0001
            else:
                print("除数不能为0")
