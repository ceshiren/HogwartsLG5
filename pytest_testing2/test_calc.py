# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 16:26
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : test_calc.py

import pytest
import allure


class TestCalc:

    @pytest.mark.usefixtures("prompt")
    @pytest.mark.run(order=1)
    @allure.story('加法测试')
    def test_add(self, instantiate_class, get_add_datas):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = instantiate_class.add(get_add_datas[0], get_add_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]

    @pytest.mark.usefixtures("prompt")
    @pytest.mark.run(order=3)
    @allure.story('乘法测试')
    def test_mul(self, instantiate_class, get_mul_datas):
        result = None
        try:
            result = instantiate_class.mul(get_mul_datas[0], get_mul_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_mul_datas[2]

    @pytest.mark.usefixtures("prompt")
    @pytest.mark.run(order=2)
    @allure.story('减法测试')
    def test_sub(self, instantiate_class, get_sub_datas):
        result = None
        try:
            result = instantiate_class.sub(get_sub_datas[0], get_sub_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_sub_datas[2]

    @pytest.mark.usefixtures("prompt")
    @pytest.mark.run(order=4)
    @allure.story('除法测试')
    def test_div(self, instantiate_class, get_div_datas):
        result = None
        try:
            result = instantiate_class.div(get_div_datas[0], get_div_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_div_datas[2]
