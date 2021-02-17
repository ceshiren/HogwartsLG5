from appium.webdriver.common.mobileby import MobileBy

from test_python.src.appium_project.pages.base_page import BasePage
from test_python.src.appium_project.pages.contact_page import ContactPage


class MainPage(BasePage):
    def goto_cantact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactPage(self.driver)