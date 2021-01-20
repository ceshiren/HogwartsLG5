import pytest
import yaml

from appium_work2.page.app import App


def get_member_info():
    with open('../data/member_info.yaml', encoding="UTF-8") as f:
        member_data = yaml.safe_load(f)
        add_data = member_data['add']
        return add_data


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum", get_member_info())
    def test_add_member(self,name,gender,phonenum):
        toast = self.main.click_contact().click_add_member().click_maual_add_member(). \
            edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save().get_toast()
        assert toast == "添加成功"
