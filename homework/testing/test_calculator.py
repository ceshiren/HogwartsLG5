# -*- coding: utf-8 -*-
# @time     : 2020/12/28 21:43
# @Author   : Owen
# @File     : test_calculator.py
import allure
import pytest


class TestCalcucator:

    @allure.feature("加法测试")
    @pytest.mark.run(order=1)
    def test_add(self, get_calculator, get_add_datas):
        '''
        这是加法测试
        '''
        result = None
        try:
            result = get_calculator.add(get_add_datas[0], get_add_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e, "加法异常，请输入正确的数字")
        else:
            print("正常加法，加法计算正确")
        assert result == get_add_datas[2]


    @allure.feature("除法测试")
    @pytest.mark.run(order=4)
    def test_div(self, get_calculator, get_div_datas):
        '''
        这是除法测试
        '''
        result = None
        try:
            result = get_calculator.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e, "除法异常，请输入正确的数字")
        else:
            print("正常除法，除法计算正确")
        assert result == get_div_datas[2]


    @allure.feature("减法测试")
    @pytest.mark.run(order=2)
    def test_sub(self, get_calculator, get_sub_datas):
        '''
        这是减法测试
        '''
        result = None
        try:
            result = get_calculator.sub(get_sub_datas[0], get_sub_datas[1])
        except Exception as e:
            print(e, "减法异常，请输入正确的数字")
        else:
            print("正常减法，减法计算正确")
        assert result == get_sub_datas[2]


    @allure.feature("乘法测试")
    @pytest.mark.run(order=3)
    def test_mul(self, get_calculator, get_mul_datas):
        '''
        这是乘法测试
        '''
        result = None
        try:
            result = get_calculator.mul(get_mul_datas[0], get_mul_datas[1])
            if isinstance(result, float):
                result = round(result, 3)
        except Exception as e:
            print(e, "乘法异常，请输入正确的数字")
        else:
            print("正常乘法，乘法计算正确")
        assert result == get_mul_datas[2]