from appium.webdriver.common.mobileby import MobileBy

from test_python.src.appium_frame.pages.addmember_page import AddMemberPage
from test_python.src.appium_frame.pages.base_page import BasePage


class ContactPage(BasePage):
    def goto_addmember(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员"))').click()
        return AddMemberPage(self.driver)