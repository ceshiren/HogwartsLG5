from selenium.webdriver.common.by import By

from homework.selenium_po.page.base_page import BasePage
from homework.selenium_po.page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)
