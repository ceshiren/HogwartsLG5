# -*- coding: utf-8 -*-
# @time     : 2021/1/17 16:05
# @Author   : Owen
# @File     : basepage.py
from typing import List

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework.test_framework_yaml.black_element import black_element


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

    def find_and_send(self, locator, value):
        return self.find(locator).send_keys(value)

    def step(self, path, operation):
        with open(path, 'r', encoding='utf-8') as f:
            datas:List[dict] = yaml.safe_load(f)
            #yaml中定义操作方式
            steps = datas[operation]
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if action == "find_and_click":
                    self.find_and_click(step["locator"])
                elif action == "click":
                    # 添加显示等待，防止弹窗元素未加载出来
                    locator = (MobileBy.ID, "iv_close")
                    WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
                    self.find(step["locator"]).click()
                elif action == "find_and_send":
                    self.find_and_send(step["locator"], step["value"])
