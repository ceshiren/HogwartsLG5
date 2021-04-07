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


class test_ddt:
    @pytest.mark.parametrize()
    def test_add(self,a,b,c):
