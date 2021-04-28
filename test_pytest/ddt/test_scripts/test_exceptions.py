#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_exceptions.py 
@Time   :   2021-04-10 10:41   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc  :    使用闭包处理异常
"""
import functools,six
import logging

import decorator

logging.basicConfig(level=logging.DEBUG)


def candy_w(func):
    @functools.wraps(func)#解决函数地址冲突问题。
    def print_candy(*args, **kwargs):
        print(*args)
        return func(*args, **kwargs)
    return print_candy