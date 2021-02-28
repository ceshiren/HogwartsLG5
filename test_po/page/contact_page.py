#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 22:11
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_po.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        pass

    def add_department(self, name):
        # 点击“+”号
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        # 点击添加部门
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        # 输入部门名称
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys(name)
        # 点击选择所属部门下拉框
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()
        # 点击第一个部门
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/div/div/ul/li/a').click()
        # 点击添加
        self.find(By.CSS_SELECTOR, '#__dialog__MNDialog__ > div > div.qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue').click()
        self.driver.refresh()
        return ContactPage(self.driver)

    def get_member_list(self):
        """
        返回通讯录页面的人员信息
        :return:
        """
        name_webelement_list = self.find(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for webelement in name_webelement_list:
            name_list.append(webelement.text)
        return name_list

    def get_department_list(self):
        locator = (By.XPATH, '//*[@class="jstree-anchor"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((locator)))
        elements = self.fine_elements(By.XPATH, '//*[@class="jstree-anchor"]')
        department_list = []
        for element in elements:
            department_list.append(element.text)

        print(department_list)
        return department_list