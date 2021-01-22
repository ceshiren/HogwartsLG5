from time import sleep

from selenium.webdriver.common.by import By

from test_python.src.selenium_programe.page.basepage import BasePage
from test_python.src.selenium_programe.page.contact_page import ContactPage


class MainPage(BasePage):
    def gotoContact(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        sleep(1)
        return ContactPage(self.driver)
    def quit(self):
        self.driver.quit()