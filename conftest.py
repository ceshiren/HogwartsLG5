#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 16:42
import pytest
from pythoncode.calculator import Calculator
import yaml
import os

yaml_file_path = os.path.dirname(__file__) + "/data.yaml"

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc

with open(yaml_file_path, 'r', encoding='UTF-8') as f:
    datas = yaml.safe_load(f)
    print(datas)
    add_datas = datas["add_datas"]
    sub_datas = datas["sub_datas"]
    mul_datas = datas["mul_datas"]
    div_datas = datas["div_datas"]
    my_ids = datas["myids"]

@pytest.fixture(params=add_datas, ids=my_ids)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")


@pytest.fixture(params=sub_datas, ids=my_ids)
def get_sub_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=mul_datas, ids=my_ids)
def get_mul_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=div_datas, ids=my_ids)
def get_div_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")