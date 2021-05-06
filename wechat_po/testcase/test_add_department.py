# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 14:41
# @Author  : Yan
# @Email   : 13433183608@163.com
# @File    : test_add_department.py
from time import sleep

from WebTestSelenium.wechat_po.page.main import Main


class TestAddDepartment():

    def setup(self):

        self.main = Main()

    def teardown(self):

        self.main._driver.quit()

    def test_add_department(self):

        result = self.main.goto_add_department().add_department("后端架构")
        sleep(2)
        res = result.get_department_list()
        assert "后端架构" in res

