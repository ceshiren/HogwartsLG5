import pytest
import yaml

from test_appium.page.app import App


def get_data(content):
    with open("../data/data.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)[content]
        print("*****")
        print(data)
        return data


class TestContact:

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.skip
    @pytest.mark.parametrize("name,gender,phonenum",get_data("add"))
    def test_add_member(self,name,gender,phonenum):
        #添加成员测试
        # name = "zhangsan3"
        # gender = "男"
        # phonenum = "13101018824"
        toast = self.main.click_addresslist().add_member().addconect_menual().edit_name(name).\
            edit_gender(gender).edit_phone(phonenum).click_save().get_toast()
        assert toast

    def test_personal_info(self):
        #查看个人信息，所属部门
        department = self.main.click_addresslist().view_personal_information("哈哈").get_department_name()
        assert department == "李佳铺子"


