#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 22:15
from test_po.page.main_page import MainPage


class TestAddMember():

    def setup_class(self):
        # 实例化MainPage类
        self.main = MainPage()

    def test_add_member(self):

        result = self.main.goto_add_member().add_member("崔丝塔娜").get_member_list()
        assert "崔丝塔娜" in result

    def test_add_member_fail(self):
        # 实例化MainPage类

        result = self.main.goto_add_member().add_member_fail("崔丝塔娜").get_member_list()
        assert "崔丝塔娜" not in result
    # def teardown_class(self):
    #     self.driver.quit()