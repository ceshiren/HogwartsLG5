#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_ddt.py 
@Time   :   2021/4/7 1:27
@Contact    :
@Author     :   WG
@Version    :   v 0.1
@Desc   :   pytest数据驱动
"""
import pytest

from test_pytest.ddt.test_scripts.test_exceptions import candy_w

class Test_ddt():
    @candy_w
    @pytest.mark.parametrize("a,b,c", [[1,2,3],(2,3,5)])
    def test_add(self,a,b,c):
        print("mission passed")
        assert a+b==c
    @candy_w
    def test_del(self):
        assert 3-1==2

