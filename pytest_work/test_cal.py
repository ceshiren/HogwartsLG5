import pytest
import yaml
from pytest_work.calculator import Calculator

with open("test_cal_data.yml") as f:
    file = yaml.safe_load(f)
    add_datas = file['add']
    sub_datas = file['sub']
    mul_datas = file['mul']
    div_datas = file['div']


class TestCal:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    # 测试add函数
    @pytest.mark.parametrize("a,b,expect", add_datas['datas'], ids=add_datas['ids'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    # 测试sub函数
    @pytest.mark.parametrize("a,b,expect", sub_datas['datas'], ids=sub_datas['ids'])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        '''
        浮点数计算不精确的问题应该在calculator中使用decimal来处理
        此处在不改变测试对象的情况下，偷懒使用round来四舍五入取值
        '''
        assert round(result, 2) == expect

    # 测试mul函数
    @pytest.mark.parametrize("a,b,expect", mul_datas['datas'], ids=mul_datas['ids'])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert round(result, 2) == expect

    # 测试div函数
    @pytest.mark.parametrize("a,b,expect", div_datas['datas'], ids=div_datas['ids'])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert round(result, 2) == expect
