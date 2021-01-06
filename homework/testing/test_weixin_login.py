# -*- coding: utf-8 -*-
# @time     : 2021/1/6 23:07
# @Author   : Owen
# @File     : test_weixin_login.py
import json
from time import sleep

from selenium import webdriver


class TestLogin():
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

    def test_cookie(self):
        # #获取  cookie
        # cookies = self.driver.get_cookies()
        # #以文件流的形式打开文件
        # with open("cookie.json", "w") as f:
        #     #存储 cookie 到 cookie.json
        #     json.dump(cookies, f)

        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流的形式打开文件
        with open("cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(2)
        self.driver.find_element_by_id("menu_customer").click()


