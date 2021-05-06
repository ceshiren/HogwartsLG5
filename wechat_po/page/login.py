# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 15:42
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : login.py
from selenium.webdriver.common.by import By

from WebTestSelenium.wechat_po.page.base_page import BasePage
from WebTestSelenium.wechat_po.page.register import Register


class Login(BasePage):

    def scan(self):

        pass

    def goto_register(self):

        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)