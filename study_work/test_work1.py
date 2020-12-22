#coding:utf-8
import pytest
import allure
from work1 import Demo
from read_yaml import *
from logs import *

@allure.feature('测试算数类')
class TestDemo:
    def setup_class(self):
        logger.info('整个测试类执行前开始执行》》》》》》》》》》》》》》》》》》》》》')
        self.demo = Demo()

    def teardown_class(self):
        logger.info('整个测试类执行前开始执行》》》》》》》》》》》》》》》》》》》》》')
        del self.demo

    def setup_method(self):
        logger.info('开始计算公式******')
        pass

    def teardown_method(self):
        logger.info('结束计算公式******')
        pass

    @allure.story('加法测试')
    @pytest.mark.parametrize(['a','b','exp'],read_yaml('add'))
    def test_add(self,a,b,exp):
        res = self.demo.add(a,b)
        assert res == exp
        logger.info(f'计算正确:计算得出{res},比较值{exp}')

    @allure.story('减法测试')
    @pytest.mark.parametrize(['a', 'b', 'exp'],read_yaml('sub'),ids=read_yaml('sub_ids'))
    def test_sub(self,a,b,exp):
        res = self.demo.sub(a, b)
        assert res == exp
        logger.info(f'计算正确:计算得出{res},比较值{exp}')

    @allure.story('乘法测试')
    @pytest.mark.parametrize(['a', 'b', 'exp'],read_yaml('mul'),ids=read_yaml('mul_ids'))
    def test_mul(self,a,b,exp):
        res = self.demo.mul(a, b)
        assert res == exp
        logger.info(f'计算正确:计算得出{res},比较值{exp}')

    @allure.story('除法测试')
    @pytest.mark.parametrize(['a', 'b', 'exp'],read_yaml('divi'),ids=read_yaml('divi_ids'))
    def test_divi(self,a,b,exp):
        res = self.demo.divi(a, b)
        assert res == exp
        logger.info(f'计算正确:计算得出{res},比较值{exp}')

if __name__ == '__main__':
    pytest.main(['test_work1.py','-sv','--alluredir=../allure_report/xml'])