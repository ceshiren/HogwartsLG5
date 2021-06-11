#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_yaml.py 
@Time   :   2021/6/11 16:50   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import yaml


def test_load_yaml():
    with open("test_yaml.yaml", "a+", encoding="utf-8") as f:
        origin = yaml.safe_load(f.read())
        print(origin)
        datas = {}
        datas["token2"] = "123"
        datas["list2"] = [1, 2, 4]
        yaml.safe_dump(datas, f)
        f.close()


def test_dump_yaml():
    with open("test_yaml.yaml", "w+", encoding="utf-8") as f:
        datas = {}
        datas["token"] = "123"
        datas["list1"] = [1, 2, 3]
        yaml.safe_dump(datas, f)
        f.close()
