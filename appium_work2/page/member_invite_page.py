from appium.webdriver.common.mobileby import MobileBy

from appium_work2.page.base_page import BasePage
from appium_work2.page.contact_edit_page import ContactEditPage


class MemberInvitePage(BasePage):
    def click_maual_add_member(self):
        add_member_locator = (MobileBy.XPATH, '//*[@text="手动输入添加"]')
        self.find_and_click(add_member_locator)
        return ContactEditPage(self.driver)

    def get_toast(self):
        toast_locator = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        ToastText = self.find_and_get_text(toast_locator)
        return ToastText
