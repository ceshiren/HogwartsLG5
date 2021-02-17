from appium.webdriver.common.mobileby import MobileBy

from test_python.src.appium_project.pages.base_page import BasePage


class MemberEditPage(BasePage):
    def messageConfirm(self):

        from test_python.src.appium_project.pages.addmember_page import AddMemberPage
        return AddMemberPage(self.driver)