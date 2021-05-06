# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 14:13
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : add_department.py
from selenium.webdriver.common.by import By

from WebTestSelenium.wechat_po.page.base_page import BasePage
from WebTestSelenium.wechat_po.page.contact import Contact


class AddDepartment(BasePage):

    def add_department(self, departname):

        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys(departname)
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id = '1688850922042169_anchor']").click()
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return Contact(self._driver)



