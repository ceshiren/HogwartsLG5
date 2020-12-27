import pytest
import os
from work2 import Demo
import yaml
from config.log_main import *

# logger = _logging()
def read_yaml(file=r'../config/work.yaml'):
    with open(file,'r') as fs :
        rs = yaml.load(fs,Loader=yaml.FullLoader)
        if rs is float:
            rs = round(rs,2)
        return rs
read_taml = read_yaml()

@pytest.fixture(scope='class')
def demo():
    '''实例化计算类'''
    demo = Demo()
    return demo

@pytest.fixture(params=read_taml['add'],ids=read_taml['add_ids'],scope='module')
def get_add_datas(request):
    '''拿到yaml加法数据'''
    logger.info('开始add计算***************************')
    read_taml = request.param
    yield read_taml
    logger.info('结束add计算***************************')

@pytest.fixture(params=read_taml['divi'],ids=read_taml['divi_ids'],scope='module')
def get_divi_datas(request):
    '''拿到yaml除法数据'''
    logger.info('开始divi计算***************************')
    read_taml = request.param
    yield read_taml
    logger.info('结束divi计算***************************')

@pytest.fixture(params=read_taml['sub'],ids=read_taml['sub_ids'],scope='module')
def get_sub_datas(request):
    '''拿到yaml减法数据'''
    logger.info('开始sub计算***************************')
    read_taml = request.param
    yield read_taml
    logger.info('结束sub计算***************************')

@pytest.fixture(params=read_taml['mul'],ids=read_taml['mul_ids'],scope='module')
def get_mul_datas(request):
    '''拿到yaml乘法数据'''
    logger.info('开始mul计算***************************')
    read_taml = request.param
    yield read_taml
    logger.info('结束mul计算***************************')

if __name__ == '__main__':
    print(read_taml)
