#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_ini.py 
@Time   :   2021/7/12 17:55   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""

import configparser

def test_read():
    config = configparser.ConfigParser()
    config.read('test.ini')
    print(config.sections())
    print(config.get('ZIP','MD5'))

# 写入ini
# 文件
# import ConfigParser

def test_write():
    config = configparser.ConfigParser()
    config.read('test.ini')
    config.add_section("book")
    config.set("book", "title", "the python standard library")
    config.set("book", "author", "fredrik lundh")
    config.add_section("ematter")
    config.set("ematter", "pages", "250")
    # write to file
    config.write(open('test.ini', "w"))

# 修改：
def test_modify():

    config = configparser.ConfigParser()
    config.read('test.ini')
    # config.add_section("md5")
    config.set("md5", "value", "123")
    config.write(open('test.ini', "w"))  # 可以把r+改成其他方式，看看结果:)
