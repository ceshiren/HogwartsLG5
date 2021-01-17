# -*- coding: utf-8 -*-
# @time     : 2021/1/17 16:30
# @Author   : Owen
# @File     : addway.py
from appium.webdriver.common.mobileby import MobileBy

from homework.appium_po.core.addmember import AddMember
from homework.appium_po.core.basepage import BasePage


class AddWay(BasePage):
    #添加成员方式
    def add_manully(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
        return AddMember(self.driver)

    #获取toast
    def get_toast(self):
        result = self.find_and_get_text((MobileBy.XPATH, '//*[contains(@text, "添加成功")]'))
        return result

    def get_abnormal_toast(self):
        abnormal_result = self.find_and_get_text((MobileBy.XPATH, '//*[contains(@text, "无法添加")]'))
        return abnormal_result