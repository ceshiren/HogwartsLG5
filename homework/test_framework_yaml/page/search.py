# -*- coding: utf-8 -*-
# @time     : 2021/1/24 10:17
# @Author   : Owen
# @File     : search.py
from appium.webdriver.common.mobileby import MobileBy

from homework.test_framework_yaml.basepage import BasePage


class Search(BasePage):

    def search(self):
        self.step("../page/search.yaml", "search")


