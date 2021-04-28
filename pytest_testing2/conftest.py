# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 15:48
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : conftest.py

import os
import pytest
import yaml
from pytest_testing1.developcode.calculator import Calculator


def get_data():
    # 通过 os.path.dirname 获取当前文件所在目录的路径
    yaml_file_path = os.path.dirname(__file__) + "/datas/calc_data.yaml"

    with open(yaml_file_path) as f:
        datas = yaml.safe_load(f)
        return datas


@pytest.fixture(scope="class")
def instantiate_class():
    # 实例化类,生成类的对象
    calc = Calculator()
    return calc

@pytest.fixture(scope="module")
def prompt():
    print("\n开始计算")
    yield
    print("\n计算结束")

@pytest.fixture(params=get_data()["add"], ids=get_data()["add_ids"], scope="module")
def get_add_datas(request):
    print('\n开始add计算***************************')
    data = request.param
    yield data
    print('\n结束add计算***************************')

@pytest.fixture(params=get_data()["sub"], ids=get_data()["sub_ids"], scope="module")
def get_sub_datas(request):
    print('\n开始sub计算***************************')
    data = request.param
    yield data
    print('\n结束sub计算***************************')

@pytest.fixture(params=get_data()["mul"], ids=get_data()["mul_ids"], scope="module")
def get_mul_datas(request):
    print('\n开始mul计算***************************')
    data = request.param
    yield data
    print('\n结束mul计算***************************')

@pytest.fixture(params=get_data()["div"], ids=get_data()["div_ids"], scope="module")
def get_div_datas(request):
    print('\n开始div计算***************************')
    data = request.param
    yield data
    print('\n结束div计算***************************')