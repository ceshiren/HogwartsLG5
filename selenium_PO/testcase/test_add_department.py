from time import sleep

from selenium_PO.page.contact_page import contact_page
from selenium_PO.page.home_page import home_page


class TestAddDepartment:
    def setup_class(self):
        self.homepage = home_page()

    def teardown_class(self):
        self.homepage.driver.quit()

    def test_add_department_successful(self):
        name = 'java组'
        result = self.homepage.click_contacts().add_department_successful(name).get_deparment_list()
        assert name in result

    def test_add_department_cancel(self):
        name = 'web组'
        result = self.homepage.click_contacts().add_department_cancel(name).get_deparment_list()
        assert name not in result

    def test_add_department_fail(self):
        name = '十大算法算法啊是发发发啊沙发沙发啊沙发沙发啊是发发发发发啊沙发沙发'
        result = self.homepage.click_contacts().add_department_fail(name)
        assert "部门名称不能超过 32 个字符" == result