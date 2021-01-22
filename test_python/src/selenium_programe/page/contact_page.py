from time import sleep

from selenium.webdriver.common.by import By

from test_python.src.selenium_programe.page.adddept_page import AddDepartmentPage
from test_python.src.selenium_programe.page.basepage import BasePage


class ContactPage(BasePage):
    def addDept(self):
        self.driver.find_element(By.CLASS_NAME, 'member_colLeft_top_addBtn').click()
        self.driver.find_element(By.CLASS_NAME, 'js_create_party').click()
        sleep(1)
        return AddDepartmentPage(self.driver)
    def getDeptList(self):
        name_webelement_list = self.finds((By.XPATH, "//*[contains(@id,'_anchor')]"))
        print(name_webelement_list)

        name_list = []
        for webelement in name_webelement_list:
            name_list.append(webelement.text)
        print("=======================")
        print(name_list)
        return name_list