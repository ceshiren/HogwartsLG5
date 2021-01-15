from selenium.webdriver.common.by import By

from seleniumpo.page.main_page import MainPage


class TestCase():
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.quit()
    #添加部门名称
    def test_add_department(self):
        result = self.main.goto_contact().add_department("产品组").get_department_list()
        assert "产品组" in result

    #部门名称为空
    def test_add_department_null(self):
        self.main.goto_contact().add_department_null("")
        result_null = self.main.find(By.ID, "js_tips").text
        assert "请输入部门名称" == result_null

    # 添加部门重复
    def test_add_department_repe(self):
        self.main.goto_contact().add_department_repe("开发部门")
        repe = self.main.find(By.ID, "js_tips").text
        assert "该部门已存在" == repe



