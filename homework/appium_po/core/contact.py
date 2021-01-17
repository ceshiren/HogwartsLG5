# -*- coding: utf-8 -*-
# @time     : 2021/1/17 16:22
# @Author   : Owen
# @File     : contact.py
from homework.appium_po.core.addway import AddWay
from homework.appium_po.core.basepage import BasePage


class Contact(BasePage):

    def add_member(self):
        self.scroll_and_find("添加成员")
        return AddWay(self.driver)