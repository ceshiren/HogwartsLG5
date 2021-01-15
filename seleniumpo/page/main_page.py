from selenium.webdriver.common.by import By

from seleniumpo.page.add_department_page import AddMemberDepartmentPage
from seleniumpo.page.base_page import BasePage


class MainPage(BasePage):
    def goto_contact(self):
        self.find(By.ID,"menu_contacts").click()
        return AddMemberDepartmentPage(self.driver)




