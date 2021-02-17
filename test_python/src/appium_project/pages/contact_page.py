from appium.webdriver.common.mobileby import MobileBy

from test_python.src.appium_project.pages.addmember_page import AddMemberPage
from test_python.src.appium_project.pages.base_page import BasePage


class ContactPage(BasePage):
    def goto_addmember(self):

        return AddMemberPage(self.driver)