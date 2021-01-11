# -*- coding: utf-8 -*-
# @time     : 2021/1/10 10:26
# @Author   : Owen
# @File     : base.py
import json
import os

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
'''
公共类用于继承
封装了cookie登录、元素定位
'''

class Base:

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver = driver

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    #cookie登录
    def _cookie_login(self):
        #获取cookie
        # cookies = self.driver.get_cookies()
        # with open("cookie.json", "w") as f:
        #     json.dump(cookies, f)
        #注入cookie
        self.driver.get("https://work.weixin.qq.com/")
        path = os.path.dirname(__file__) + "./cookie.json"
        with open(path, 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    #封装元素定位
    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)
