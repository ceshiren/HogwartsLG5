from selenium import webdriver
from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class MainPage(BasePage):

    def goto_contact(self):
        self.find(By.ID,"menu_contacts").click()
        return ContactPage(self.driver)
