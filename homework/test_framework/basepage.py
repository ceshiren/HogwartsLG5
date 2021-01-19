# -*- coding: utf-8 -*-
# @time     : 2021/1/17 16:05
# @Author   : Owen
# @File     : basepage.py
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from homework.test_framework.page.black_element import black_element


class BasePage:

    def __init__(self, driver: WebDriver=None):
        self.driver = driver

    #封装黑名单元素查找
    @black_element
    def find(self, locator):
        element = self.driver.find_element(*locator)
        return element


    def find_and_click(self, locator):
        return self.find(locator).click()

    #滚动查找元素
    def scroll_and_find(self,text):
        return self.find((MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
                                                       f'.text("{text}").instance(0));')).click()
    #获取toast文本
    def find_and_get_text(self, locator):
        return self.find(locator).text


