import pytest
import yaml

from appiumpo.page.app import App


def get_data():
    with open('../data/data.yml',encoding="UTF-8") as i:
        data = yaml.safe_load(i)
        add_data = data["add"]
        return add_data

class TestContact:
    def setup(self):
        # App实例化
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phone",get_data())
    def test_add_contact(self,name ,gender,phone):
        # name="可可西里5"
        # gender="女"
        # phone="13322220222"
        toast = self.main.click_addresslist().add_member().addconect_menual().\
            edit_name(name).edit_gender(gender).edit_phone(phone).click_save().get_toast()
        assert toast == "添加成功"

if __name__ == '__main__':
    print(get_data()['add'])