"""
__author__ = 'jaxon'
__time__ = '2021/1/16 下午8:48'
__desc__ = ''
"""
import pytest
import yaml

from test_appium.page.app import App

def get_data():
    with open('../data/data.yaml',encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        add_data = data['add']
        return add_data


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum",get_data())
    def test_add_contact(self,name,gender,phonenum):
        # name = "zhangsi2"
        # gender = '男'
        # phonenum = '13300000002'
        toast = self.main.click_addresslist().add_member().addconect_menual().\
            edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save().get_toast()
        assert toast == "添加成功"

if __name__ == '__main__':
    print(get_data()['add'])