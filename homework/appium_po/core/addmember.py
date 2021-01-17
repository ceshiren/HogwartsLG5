# -*- coding: utf-8 -*-
# @time     : 2021/1/17 16:33
# @Author   : Owen
# @File     : addmember.py


from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework.appium_po.core.basepage import BasePage

class AddMember(BasePage):

    def add_name(self, name):
        self.find((MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText')).send_keys(name)
        return self

    def add_gender(self, gender):
        self.find((MobileBy.XPATH, '//*[@text="男"]')).click()
        if gender == "男":
            locator = (MobileBy.XPATH, '//*[contains(@text,"男")]')
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
            self.find_and_click((MobileBy.XPATH, '//*[contains(@text,"男")]'))

        else:
            locator = (MobileBy.XPATH, '//*[contains(@text,"女")]')
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
            self.find_and_click((MobileBy.XPATH, '//*[contains(@text,"女")]'))
        return self

    def add_phone_number(self, number):
        self.find((MobileBy.XPATH, '//*[@text="手机号"]')).send_keys(number)
        return self

    def click_and_save(self):
        self.find((MobileBy.XPATH, '//*[@text="保存"]')).click()
        # 局部导包
        from homework.appium_po.core.addway import AddWay
        return AddWay(self.driver)

















