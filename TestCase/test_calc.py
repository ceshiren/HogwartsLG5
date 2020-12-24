# coding:utf-8
# Name:test_calc.py
# Author:qi.yu
# Time:2020/12/23 9:57 上午
# Description:

import pytest
import allure
import yaml

from calculator import Calculator

@allure.feature('加减乘除模块')
class TestCalc:

    def setup_class(self):
        print('测试开始--类级别')
        self.calc = Calculator()

    def teardown_class(self):
        print('测试结束--类级别')

    def setup(self):
        print('开始计算')

    def teardown(self):
        print("\r\n计算结束")

    @pytest.mark.calc
    @allure.story('加法测试')
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./TestData/add.yml'))['data'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.calc
    @allure.story('减法测试')
    @pytest.mark.parametrize('a,b,expect', [(2, 1, 1), (-1, -2, 1)])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.calc
    @allure.story('乘法测试')
    @pytest.mark.parametrize('a, b, expect', [(1, 2, 2), (-2, -5, 10)])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.calc
    @allure.story('除法测试')
    @pytest.mark.parametrize('a, b, expect', [(1, 2, 0.5), (-10, -5, 2)])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect


if __name__ == '__main__':
    pytest.main(['-sv', 'test_calc.py::TestCalc::test_add', '--alluredir', '../Report'])
