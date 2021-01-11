# -*- coding: utf-8 -*-
# @time     : 2021/1/10 11:16
# @Author   : Owen
# @File     : test_add_department.py
from homework.weixin.core.mainpage import MainPage


class TestDepartment:

    def setup(self):
        self.mainpage = MainPage()

    def teardown(self):
        self.mainpage.driver.quit()

    def test_department(self):
        result = self.mainpage.goto_contact().add_department("SQA").get_department()
        assert "SQA" in result

    def test_department_fail(self):
        result = self.mainpage.goto_contact().add_department_fail("SQA").get_department()
        assert result.count("SQA") == 1


