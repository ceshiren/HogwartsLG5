import pytest
import yaml
from appium_work1.page.app import App

class TestAddMember:

    def setup(self):
        self.app = App()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize(['name','sex','phone'],yaml.safe_load(open('../page/add_member_params.yaml','r',encoding='utf-8')),ids=['add1','add2'])
    def test_add_member_success(self,name,sex,phone):
        toeast = self.app.start().main().goto_contact().goto_add_member().manual_add_member().send_name(name)\
                      .choice_sex(sex).send_phone(phone).click_save().add_member_toeast()
        pytest.assume(toeast == '添加成功')

if __name__ == '__main__':
        pytest.main(['test_add_member.py','-sv'])