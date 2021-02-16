from homework.selenium_po.page.main_page import MainPage


class TestAddDepartment:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        # self.main.driver.quit()
        pass

    def test_add_department(self):
        # 用例测试过程和测试结果判断
        result = self.main.goto_contact().goto_add_department().add_department().get_department_list()
        assert '测试部' in result
