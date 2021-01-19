# -*- coding: utf-8 -*-
# @time     : 2021/1/19 22:37
# @Author   : Owen
# @File     : search.py
from appium.webdriver.common.mobileby import MobileBy

from homework.test_framework.basepage import BasePage


class Search(BasePage):

    def get_text(self):
        result = self.find((MobileBy.XPATH, '//*[@text="今日热点"]')).text
        return result