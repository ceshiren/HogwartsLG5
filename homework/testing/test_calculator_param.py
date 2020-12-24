# -*- coding: utf-8 -*-
# @time     : 2020/12/23 16:30
# @Author   : Owen
# @File     : test_calculator_param.py
import pytest
import os, sys

#导包加入 sys.path ,保证脚本在terminal中正常运行
path = sys.path[0]
for i in range(2):
    path = os.path.dirname(path)
    sys.path.append(path)

from homework.src.calculator import Calculator

class TestCalcucator:

    def setup_class(self):
        #实例化对象
        print("调用计算机加法和除法进行计算")
        self.calculator = Calculator()

    def teardown_class(self):
        print("计算全部完成")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")
    #正常加法
    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (1000, 1000, 2000),
        (-1, -2, -3),
        (-5, 4, -1),
        (2, 0, 2),
        (-5, 0, -5),
        (2, 0.5, 2.5),
        (0.5, 0.5, 1.0),
        (-0.3, 1, 0.7),
        (-0.5, -0.5, -1.0),
        (-0.5, 0, -0.5),
        (0.4, 0, 0.4)
    ])
    def test_add1(self, a, b, expected):
        print("正常加法，加法计算正确")
        result = self.calculator.add(a, b)
        assert result == expected

    #异常加法，类型错误
    @pytest.mark.parametrize("a, b", [
        (1, "a"),
    ])
    def test_add2(self, a, b):
        print("异常加法，类型错误")
        with pytest.raises(TypeError):
            1 + "a"
    #正常除法
    @pytest.mark.parametrize("a, b, expected", [
        (4, 2, 2.0),
        (1000, 2, 500.0),
        (5, 2.5, 2.0),
        (2.5, 0.5, 5.0),
        (6, -2, -3.0),
        (-8, -4, 2.0),
        (-6, 1.5, -4.0),
        (0, 1, 0.0),
        (0, -2, -0.0),
        (0, 0.5, 0.0),
        (0, -0.4, -0.0),
        (0, -0.4, -0.0)
    ])
    def test_div1(self, a, b, expected):
        print("正常除法，除法计算正确")
        result = self.calculator.div(a, b)
        assert result == expected
    #异常除法，类型错误
    @pytest.mark.parametrize("a, b", [
        (1, "a")
    ])
    def test_div2(self, a, b):
        print("异常除法,类型错误")
        with pytest.raises(TypeError):
            1 / "a"
    #除零错误
    def test_zero_division(self):
        print("除零错误")
        with pytest.raises(ZeroDivisionError):
            1 / 0