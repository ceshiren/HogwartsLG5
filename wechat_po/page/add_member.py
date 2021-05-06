# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 14:13
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : add_member.py
from selenium.webdriver.common.by import By

from WebTestSelenium.wechat_po.page.base_page import BasePage
from WebTestSelenium.wechat_po.page.contact import Contact


class AddMember(BasePage):

    def add_member(self):

        # 输入成员信息，点击保存
        self.find(By.ID, "username").send_keys("喻宝")
        self.find(By.ID, "memberAdd_acctid").send_keys("yubao@hongyu.com")
        self.find(By.ID, "memberAdd_phone").send_keys("13923205606")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact(self._driver)

    # def add_member_fail(self):
    #     # 输入成员信息，点击保存
    #     # *代表解元祖，相当于self.find(By.ID, "username")
    #     self.find(By.ID, "username").send_keys("喻思宏")
    #     self.find(By.ID, "memberAdd_acctid").send_keys("yusihong@hongyu.com")
    #     self.find(By.ID, "memberAdd_phone").send_keys("13923205604")
    #     self.find(By.CSS_SELECTOR, ".js_btn_save").click()
    #     self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
    #     return Contact(self._driver)