# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 15:21
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : main.py
from time import sleep

from selenium.webdriver.common.by import By

from WebTestSelenium.wechat_po.page.add_department import AddDepartment
from WebTestSelenium.wechat_po.page.add_member import AddMember
from WebTestSelenium.wechat_po.page.base_page import BasePage
from WebTestSelenium.wechat_po.page.login import Login
from WebTestSelenium.wechat_po.page.register import Register
from WebTestSelenium.wechat_po.page.contact import Contact


class Main(BasePage):

    # _base_url = "https://work.weixin.qq.com/"
    # _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_register(self):

        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)


    def goto_login(self):

        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)

    def goto_contact(self):

        return self.find(By.CSS_SELECTOR, "#menu_contacts > span").click()

    def goto_add_member(self):

        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap").click()
        return AddMember(self._driver)

    def goto_add_department(self):

        self.goto_contact() #点击通讯录
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap").click()  # 点击添加按钮
        self.find(By.CSS_SELECTOR, ".js_create_party").click()  # 点击添加部门
        return AddDepartment(self._driver)