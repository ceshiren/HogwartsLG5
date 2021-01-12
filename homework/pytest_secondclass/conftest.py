# -*- coding: utf-8 -*-

import pytest
import yaml
import os
from homework.pytest_firstclass.code.calculator import Calculator


@pytest.fixture(scope="module")
def get_calc():
    calc = Calculator()
    return calc

# 获取conftest.py文件的绝对路径
yaml_filepath = os.path.dirname(__file__) + '/testdata.yml'

with open(yaml_filepath, encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    print(datas)
    add_datas = datas['add_datas']
    sub_datas = datas['sub_datas']
    mul_datas = datas['mul_datas']
    div_datas = datas['div_datas']
    ids = datas['caseid']

@pytest.fixture(scope="module")
def start_end_perform():
    print("开始计算")
    yield
    print("结束计算")

@pytest.fixture(params=add_datas, ids=ids)
def get_adddatas(request):
    data = request.param
    yield data

@pytest.fixture(params=sub_datas, ids=ids)
def get_subdatas(request):
    data = request.param
    yield data

@pytest.fixture(params=mul_datas, ids=ids)
def get_muldatas(request):
    data = request.param
    yield data

@pytest.fixture(params=div_datas, ids=ids)
def get_divdatas(request):
    data = request.param
    yield data