#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_cal.py 
@Time   :   2021/5/11 20:45   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
def a1():
    pass

a = 1234
def func1(b,a1):
    global a
    print(b is a)
    a = "hello"
    print(b is a)
func1(a,func1(a,a1()))
"""
> 
True
False
"""