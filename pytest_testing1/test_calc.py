# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 16:26
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : test_calc.py

import pytest

from pytest_testing1.developcode.calculator import Calculator
from pytest_testing1.get_datas import get_datas


class TestCalc:

    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    def setup_method(self):
        print("\n开始计算")
    def teardown_method(self):
        print("\n计算结束")

    # 使用参数化
    @pytest.mark.parametrize("a , b, expect",
                             get_datas()['add'],
                             ids = get_datas()['add_ids'])
    def test_add(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    # 使用参数化
    @pytest.mark.parametrize("a , b, expect",
                             get_datas()['sub'],
                             ids = get_datas()['sub_ids'])
    def test_sub(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.sub(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    # 使用参数化
    @pytest.mark.parametrize("a , b, expect",
                             get_datas()['mul'],
                             ids = get_datas()['mul_ids'])
    def test_mul(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.mul(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    # 使用参数化
    @pytest.mark.parametrize("a , b, expect",
                             get_datas()['div'],
                             ids = get_datas()['div_ids'])
    def test_div(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.div(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect