# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_scope.py
import pytest




class TestDemo:

    def test_a(self, connectDB):
        print("测试用例a")

    def test_b(self, connectDB):
        print("测试用例b")

class TestDemo2:

    def test_a(self):
        print("测试用例a")

    def test_b(self):
        print("测试用例b")