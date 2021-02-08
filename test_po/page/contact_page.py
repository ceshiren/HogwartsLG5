import time

from selenium.webdriver.common.by import By

from test_po.page.add_department_page import AddDepartmentPage
from test_po.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_department(self):
        time.sleep(3)
        self.find(By.CSS_SELECTOR,".js_create_dropdown").click()
        self.find(By.CSS_SELECTOR,".js_create_party").click()
        return AddDepartmentPage(self.driver)

    def get_department_list(self):
        result = []
        departments = self.finds(By.CSS_SELECTOR,'.jstree-anchor')
        for department in departments:
            result.append(department.text)
        # print(result)
        return result