from test_po.page.contact_page import ContactPage
from test_po.page.main_page import MainPage
import pytest


class TestAddDepartment():

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    def test_add_department(self):
        # result = True
        self.main.goto_contact().goto_add_department().add_department("产品部门")
        result = ContactPage(self.main.driver).get_department_list()
        assert "产品部门" in result
