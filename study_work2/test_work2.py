#coding:utf-8
import pytest
import allure
from work2 import Demo
from config.log_main import *
@allure.feature('测试算数类')
class TestDemo:
    @pytest.mark.run(order=1)
    @allure.story('加法测试')
    def test_add(self,demo,get_add_datas):
        res = demo.add(get_add_datas[0],get_add_datas[1])
        assert res == get_add_datas[2]
        logger.info(f'计算正确:计算得出{res},比较值{get_add_datas[2]}')

    @pytest.mark.run(order=4)
    @allure.story('除法测试')
    def test_divi(self,demo,get_divi_datas):
        res = demo.divi(get_divi_datas[0],get_divi_datas[1])
        assert res == get_divi_datas[2]
        logger.info(f'计算正确:计算得出{res},比较值{get_divi_datas[2]}')

    @pytest.mark.run(order=2)
    @allure.story('减法测试')
    def test_sub(self,demo,get_sub_datas):
        res = demo.sub(get_sub_datas[0],get_sub_datas[1])
        assert res == get_sub_datas[2]
        logger.info(f'计算正确:计算得出{res},比较值{get_sub_datas[2]}')

    @pytest.mark.run(order=3)
    @allure.story('乘法测试')
    def test_mul(self,demo,get_mul_datas):
        res = demo.mul(get_mul_datas[0],get_mul_datas[1])
        assert res == get_mul_datas[2]
        logger.info(f'计算正确:计算得出{res},比较值{get_mul_datas[2]}')

if __name__ == '__main__':
    pytest.main(['test_work2.py','-sv','--alluredir=../allure_report/xml'])
