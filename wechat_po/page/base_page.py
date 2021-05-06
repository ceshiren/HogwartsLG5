# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 15:23
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : base_page.py
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    _base_url = ""

    def __init__(self, driver:WebDriver=None):

        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._cookie_login()
            # 复用 debug 浏览器
            # chrome_args = webdriver.ChromeOptions()
            # chrome_args.debugger_address = "127.0.0.1:9222"
            # self._driver = webdriver.Chrome(options=chrome_args)
        else:
            self._driver = driver
        self._driver.implicitly_wait(3)
        # if self._base_url != "":
        #     self._driver.get(self._base_url)

    def _cookie_login(self):
        self._driver.get("https://work.weixin.qq.com/")
        # 以文件流的形式打开文件
        with open("../data/cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self._driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def find(self, by, locator):

        return self._driver.find_element(by, locator)

    def finds(self, by, locator):

        return self._driver.find_elements(by, locator)