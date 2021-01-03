import pytest
import yaml
from pytest_work.calculator import Calculator
import os

yaml_file_path = os.path.dirname(__file__) + "/test_cal_data.yml"
# 打开yaml文件，并获取对应key值
with open(yaml_file_path) as f:
    file = yaml.safe_load(f)
    add_datas = file['add']
    sub_datas = file['sub']
    mul_datas = file['mul']
    div_datas = file['div']


# 声明Caculator类对象并返回
@pytest.fixture(scope='module')
def get_cal():
    calc = Calculator()
    return calc


# 活动add的测试数据
@pytest.fixture(params=add_datas['datas'], ids=add_datas['ids'])
def get_add_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


@pytest.fixture(params=sub_datas['datas'], ids=sub_datas['ids'])
def get_sub_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


@pytest.fixture(params=mul_datas['datas'], ids=mul_datas['ids'])
def get_mul_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


@pytest.fixture(params=div_datas['datas'], ids=div_datas['ids'])
def get_div_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")
