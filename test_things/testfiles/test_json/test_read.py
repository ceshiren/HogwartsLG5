#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_json.py
@Time   :   2021/4/15 16:40   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import json


def test_read_res():
    with open("res.json", encoding='utf-8') as f:
        datas = json.load(f)
        f.close()
    print(datas)