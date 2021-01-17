# -*- coding: utf-8 -*-
# @time     : 2021/1/17 16:16
# @Author   : Owen
# @File     : mainpage.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework.appium_po.core.basepage import BasePage
from homework.appium_po.core.contact import Contact


class MainPage(BasePage):

    def goto_contact(self):
        locator = (MobileBy.XPATH, '//*[@text="通讯录"]')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return Contact(self.driver)