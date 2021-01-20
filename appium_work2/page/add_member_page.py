from appium.webdriver.common.mobileby import MobileBy
from appium_work2.page.base_page import BasePage
from appium_work2.page.member_invite_page import MemberInvitePage


class AddMemberPage(BasePage):
    def click_add_member(self):
        self.scroll_find_click("添加成员")
        return MemberInvitePage(self.driver)


