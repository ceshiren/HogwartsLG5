#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 16:15

from test_po.page.main_page import MainPage


class TestAddDepartment():

    def setup_class(self):
        # 实例化MainPage类
        self.main = MainPage()

    def test_add_deprtment(self):

        result = self.main.goto_contact().add_department('测试测试').get_department_list()
        assert "测试测试" in result

