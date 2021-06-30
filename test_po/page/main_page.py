from selenium import webdriver
from selenium.webdriver.common.by import By

from test_po.page.add_member_page import AddMemberPage
from test_po.page.base_page import BasePage


class MainPage(BasePage):
    def goto_contact(self):
        pass

    def goto_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()

        # 快捷键 alt+回车可以快捷导入
        return AddMemberPage(self.driver)

