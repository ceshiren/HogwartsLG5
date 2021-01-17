# -*- coding: utf-8 -*-
# @time     : 2021/1/17 16:51
# @Author   : Owen
# @File     : test_addmember.py
import pytest
import yaml

from homework.appium_po.core.app import App

def get_data():
    with open("../core/data.yaml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        normal_data = datas["normal_data"]
        duplicate_data = datas["duplicate_data"]
    return [normal_data, duplicate_data]

class TestAddMember:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name, gender, number", get_data()[0])
    def test_addmember(self, name, gender, number):
        toast = self.main.goto_contact().add_member(). \
            add_manully().add_name(name).add_gender(gender).add_phone_number(number).click_and_save().get_toast()
        assert toast == "添加成功"

    @pytest.mark.parametrize("name, gender, number", get_data()[1])
    def test_addmember_fail(self, name, gender, number):
        toast = self.main.goto_contact().add_member(). \
            add_manully().add_name(name).add_gender(gender).add_phone_number(number).click_and_save().get_abnormal_toast()
        assert toast ==  "手机已存在于通讯录，无法添加"