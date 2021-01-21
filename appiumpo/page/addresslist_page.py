from appium.webdriver.common.mobileby import MobileBy

from appiumpo.page.base_page import BasePage
from appiumpo.page.memberinvite_page import MemberinvitePage

#点击添加成员
class AddresslistPage(BasePage):
    def add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        self.scroll_find_click("添加成员")
        return MemberinvitePage(self.driver)