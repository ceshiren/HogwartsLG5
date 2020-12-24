# -*- coding: utf-8 -*-
# @time     : 2020/12/23 16:48
# @Author   : Owen
# @File     : test_calculator_param_yaml.py
import pytest
import os, sys
import yaml

#导包加入 sys.path ,保证脚本在terminal中正常运行
path = sys.path[0]
for i in range(2):
    path = os.path.dirname(path)
    sys.path.append(path)

from homework.src.calculator import Calculator

#把yaml数据用函数进行封装
def get_datas():
    with open("./data.yaml") as f:
        datas = yaml.safe_load(f)
        #获取文件中key为datas的数据
        add_datas = datas["datas"]["add"]
        div_datas = datas["datas"]["div"]
        return [add_datas,div_datas]


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
    @pytest.mark.parametrize("a, b, expected", get_datas()[0])
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
    @pytest.mark.parametrize("a, b, expected", get_datas()[1])
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
