from appium.webdriver.common.mobileby import MobileBy

from test_python.src.appium_project.pages.base_page import BasePage
from test_python.src.appium_project.pages.memberedit_page import MemberEditPage


class AddMemberPage(BasePage):
    def goto_memberedit(self):

        return MemberEditPage(self.driver)