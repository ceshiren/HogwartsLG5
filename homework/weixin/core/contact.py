# -*- coding: utf-8 -*-
# @time     : 2021/1/10 11:03
# @Author   : Owen
# @File     : contact.py
'''
联系人页面
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

from homework.weixin.core.base import Base



class Contact(Base):
    _username = (By.NAME, "name")
    #添加部门
    def add_department(self, name):

        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        self.find(*self._username).send_keys(name)
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688853158916435_anchor"]').click()
        self.find(By.CSS_SELECTOR, '[d_ck=submit]').click()
        self.driver.refresh()
        return self

    #获取部门元素列表
    def get_department(self):
        locator = (By.XPATH, '//*[@class="jstree-anchor"]')
        WebDriverWait(self.driver, 10).until(E.visibility_of_element_located((locator)))
        elements = self.driver.find_elements(By.XPATH, '//*[@class="jstree-anchor"]')
        department_list = []
        for element in elements:
            department_list.append(element.text)
        return department_list

    #重复部门添加
    def add_department_fail(self, name):

        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        self.find(*self._username).send_keys(name)
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688853158916435_anchor"]').click()
        self.find(By.CSS_SELECTOR, '[d_ck=submit]').click()
        self.driver.refresh()
        return self