# -*- coding: utf-8 -*-
# @time     : 2021/1/19 22:27
# @Author   : Owen
# @File     : mainpage.py


from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework.test_framework_yaml.basepage import BasePage
from homework.test_framework_yaml.page.search import Search


class MainPage(BasePage):

    def goto_search(self):
        self.step("../page/mainpage.yaml", "goto_search")
        return Search(self.driver)



