#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 22:11
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_po.page.add_member_page import AddMemberPage
from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class MainPage(BasePage):

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()

        return AddMemberPage(self.driver)