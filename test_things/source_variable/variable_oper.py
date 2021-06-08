#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   variable_oper.py 
@Time   :   2021/5/7 20:26   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   设置/读取环境变量
"""
import os

import pytest


def test_ok():
    print("pass test")
    assert True

def test_variable_oper():
    print(os.getenv("PATH"))#获取环境变量
    os.environ["wg"] = "variable_wg"#设置环境变量
    print(os.getenv("wg"))
    os.environ["wg"] = "variable_wg1"#重复设置环境变量
    print(os.getenv("wg"))
    dic11 = {"wg2":"variable2"}
    os.putenv("wg3","123")#不推荐使用。
    print(os.getenv("wg3"))
    pytest.xfail()
    assert 1==2
