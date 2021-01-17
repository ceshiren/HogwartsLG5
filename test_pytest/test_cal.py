import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    #  使用参数化
    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(10000,10000,20000)])
    # 测试add函数
    def test_add(self,a,b,expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a,b)
        # 判断result结果是否等于期望的值
        assert result == expect
