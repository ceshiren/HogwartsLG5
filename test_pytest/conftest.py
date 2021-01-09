# -*- coding: utf-8 -*-
# @Author : feier
# @File : conftest.py
import pytest
import yaml

# from test_pytest.pythoncode.calculator import Calculator
import os

# 通过 os.path.dirname 获取当前文件所在目录的路径
yaml_file_path = os.path.dirname(__file__) + "/data.yml"

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    print(datas)
    # 获取文件中key为datas的数据
    add_datas = datas["datas"]
    # 获取文件中key为myids的数据
    add_ids = datas["myids"]

@pytest.fixture(params=add_datas, ids=add_ids)
def get_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")

# @pytest.fixture(scope="class")
# def get_calc():
#     print("获取计算器实例")
#     calc = Calculator()
#     return calc