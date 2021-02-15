from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class PersonalInfoPage(BasePage):
    def get_department_name(self):
        return self.find_and_get_text((MobileBy.ID,"com.tencent.wework:id/bf6"))