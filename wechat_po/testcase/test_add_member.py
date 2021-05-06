# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 16:31
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : test_add_member.py
from WebTestSelenium.wechat_po.page.main import Main


class TestAddMember():

    def setup(self):

        self.main = Main()

    def teardown(self):

        self.main._driver.quit()

    def test_add_member(self):

        # 1.首页跳转到添加成员页面 2.添加成员 3.获取成员信息
        result =self.main.goto_add_member().add_member().get_member_list()
        assert "肚肚" in result

    # def test_add_member_fail(self):
    #
    #     # 1. 描述业务场景， 不是描述具体的行为操作
    #     result = self.main.goto_add_member().add_member_fail("喻思南").get_list()
    #     assert "喻思南" not in result