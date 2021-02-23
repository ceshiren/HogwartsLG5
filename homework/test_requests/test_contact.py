# -*- coding: utf-8 -*-
# @time     : 2021/2/23 22:08
# @Author   : Owen
# @File     : test_contact.py
import requests


class TestContact:
    #获取token
    def test_get_token(self):
        id = 'ww2d28db204b542dba'
        secret = 'ocBS9XopZKd_wvFqZABXnr469liKHQK9UftZIhH3UBY'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}'
        r = requests.get(url)
        return r.json()['access_token']

    #添加成员
    def test_add_contact(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}'
        body = {
            "userid": "xiaoyan1",
            "name": "萧炎1",
            "mobile": "+86 13800001235",
            "department": [1]
        }
        r = requests.post(url, json=body)
        assert r.json()["errcode"] == 0
        return print(r.json())

    #删除成员
    def test_del_contact(self):
        id = 'xiaoyan1'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.test_get_token()}&userid={id}'
        r = requests.get(url)
        assert r.json()["errcode"] == 0
        return print(r.json())

    #修改成员信息
    def test_modify_contact(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.test_get_token()}'
        body = {
            "userid": "xiaoyan",
            "name": "小严",
        }
        r = requests.post(url, json=body)
        assert r.json()["errcode"] == 0
        return print(r.json())

    #获取成员信息
    def test_get_contact(self):
        id = 'xiaoyan'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.test_get_token()}&userid={id}'
        r = requests.get(url)
        assert r.json()["errcode"] == 0
        return print(r.json())

