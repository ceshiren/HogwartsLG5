# _*_encoding=utf-8_*_

import pytest
import yaml
from homework.pytest_firstclass.code.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("\n开始计算")

    def teardown(self):
        print("\n计算结束")

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open('./testdata.yml'))['add_datas'],
                             ids=yaml.safe_load(open('./testdata.yml'))['caseid'],
                             )
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open('./testdata.yml'))['sub_datas'],
                             ids=yaml.safe_load(open('./testdata.yml'))['caseid'],
                             )
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open('./testdata.yml'))['mul_datas'],
                             ids=yaml.safe_load(open('./testdata.yml'))['caseid'],
                             )
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open('./testdata.yml'))['div_datas'],
                             ids=yaml.safe_load(open('./testdata.yml'))['caseid'],
                             )
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect