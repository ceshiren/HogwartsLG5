#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 22:53
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHomework:

    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_click(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()
        time.sleep(3)
        with open("cookie.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]').click()
        time.sleep(3)