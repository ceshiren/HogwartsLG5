import yaml
import os
import pytest

# 通过os.path.dirname 获取当前文件所在路径


from homework_zfh.calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + r"\data.yml"
print(yaml_file_path)
# 打开yml文件
with open(yaml_file_path, mode='r', encoding='UTF-8') as f:
    datas = yaml.safe_load(f)
    print(datas)
    # 获取文件的datas数据
    add_datas = datas["add_data"]
    sub_datas = datas["sub_data"]
    mul_datas = datas["mul_data"]
    div_datas = datas["div_data"]

# 加取减法数据
@pytest.fixture(params=add_datas)
def add_datas(request):
    print("开始计算")
    # 获取参数列表中的值
    add_data = request.param
    yield add_data
    print("结束计算")
# 获取减法数据
@pytest.fixture(params=sub_datas)
def sub_datas(request):
    print("开始计算")
    sub_data = request.param
    yield sub_data
    print("结束计算")

@pytest.fixture(params=mul_datas)
def mul_datas(request):
    print("开始计算")
    mul_data = request.param
    yield mul_data
    print("结束计算")

@pytest.fixture(params=div_datas)
def div_datas(request):
    print("开始计算")
    div_data = request.param
    yield div_data
    print("结束计算")



@pytest.fixture(scope="module")
def get_cal():
    # 获取计算器实例
    cal = Calculator()
    return cal