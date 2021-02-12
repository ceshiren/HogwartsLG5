from selenium.webdriver.common.by import By

from test_python.src.wechart.page.contacts_page import Contacts
from test_python.src.wechart.page.base_page import BasePage


class IndexPage(BasePage):
    def goto_contacts(self):
        self.click_element_by(By.ID, 'menu_contacts')
        return Contacts(self.driver)
