import pytest
import yaml
from homework.app_po.page.app import App

def get_data():
    with open("../data/data.yaml", 'r', encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data

class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,email", get_data()['add'])
    def test_add_member(self, name, gender, email):
        # name = "zhangsan4"
        # gender = "女"
        # email = "zhangsan4@qq.com"
        toast = self.main.goto_contact().goto_add_member().\
            goto_manual_add_member_page().edit_name(name).edit_gender(gender).\
            edit_email(email).click_save().get_toast()
        assert toast == "添加成功"