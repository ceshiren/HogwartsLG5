#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 22:55
import json

from selenium import webdriver

def get_cookie():

    chrome_arg = webdriver.ChromeOptions()
    chrome_arg.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=chrome_arg)

    driver.get("https://work.weixin.qq.com/wework_admin/frame")

    cookies = driver.get_cookies()
    with open("cookie.json", "w") as f:
        json.dump(cookies, f)

if __name__ == '__main__':

    get_cookie()