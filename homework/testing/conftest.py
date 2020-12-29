# -*- coding: utf-8 -*-
# @time     : 2020/12/28 21:42
# @Author   : Owen
# @File     : conftest.py
import os
import sys

import pytest

import yaml

#导包加入 sys.path ,保证脚本在terminal中正常运行
path = sys.path[0]
for i in range(2):
    path = os.path.dirname(path)
    sys.path.append(path)
from homework.src.calculator import Calculator

# 通过 os.path.dirname 获取当前文件所在目录的路径
yaml_file_path = os.path.dirname(__file__) + "\\data1.yaml"

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    # 获取文件中key为add、div的数据
    add_datas = datas["add"]
    div_datas = datas["div"]
    sub_datas = datas["sub"]
    mul_datas = datas["mul"]

@pytest.fixture(params=add_datas)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是: {data}")
    yield data
    print("结束计算")

@pytest.fixture(params=div_datas)
def get_div_datas(request):
    print("开始计算")
    data1 = request.param
    print(f"request.param的测试数据是: {data1}")
    yield data1
    print("结束计算")

@pytest.fixture(params=sub_datas)
def get_sub_datas(request):
    print("开始计算")
    data2 = request.param
    print(f"request.param的测试数据是: {data2}")
    yield data2
    print("结束计算")

@pytest.fixture(params=mul_datas)
def get_mul_datas(request):
    print("开始计算")
    data3 = request.param
    print(f"request.param的测试数据是: {data3}")
    yield data3
    print("结束计算")

@pytest.fixture(scope="module")
def get_calculator():
    print("获取计算器实例")
    calculator = Calculator()
    return calculator

