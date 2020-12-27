#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/27 17:40
import pytest
from pythoncode.calculator import Calculator
class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def setup_method(self):
        print("【开始计算】")

    def teardown_method(self):
        print("【计算结束】")

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 8), (-1, -2, -3), (10000, 10000, 20000)])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [(3, 5, -2), (-1, -2, 1), (10000, 10000, 0)])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 15), (-1, -2, 2), (10000, 10000, 100000000)])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 0.6), (-1, -2, 0.5), (10000, 10000, 1)])
    def test_mul(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect