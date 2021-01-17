# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_calc_new.py
import pytest
import yaml


class TestCalc:

    # 测试add函数
    def test_add(self, get_calc, get_datas):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = get_calc.add(get_datas[0],get_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_datas[2]