# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 14:19
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : contact.py
from time import sleep

from selenium.webdriver.common.by import By

from WebTestSelenium.wechat_po.page.base_page import BasePage


class Contact(BasePage):

    def goto_add_member(self):

        pass

    def get_member_list(self):

        """
        返回通讯录页面的人员信息
        :return:
        """
        name_element_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for element in name_element_list:
            name_list.append(element.text)
        return name_list

    def get_department_list(self):

        name_element_list = self.finds(By.XPATH, '//ul[@role="group" and @class="jstree-children"]//li')
        name_list = []
        for element in name_element_list:
            name_list.append(element.text.strip())
        return name_list
