from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_work2.page.base_page import BasePage


class ContactEditPage(BasePage):
    def edit_name(self, name):
        name_locator = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
        self.find(name_locator).send_keys(name)
        return self

    def edit_gender(self, gender):
        women_locator = (MobileBy.XPATH, "//*[@text='女']")
        man_locator = (MobileBy.XPATH, "//*[@text='男']")
        gender_locator = (MobileBy.XPATH, "//*[@text='男']")
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(gender_locator))
        ele.click()
        if gender == '女':
            self.find_and_click(women_locator)
        else:
            self.find_and_click(man_locator)
        return  self

    def edit_phonenum(self, phonenum):
        phonenum_locator = (MobileBy.ID, "com.tencent.wework:id/fuy")
        self.find(phonenum_locator).send_keys(phonenum)
        return self

    def click_save(self):
        from appium_work2.page.member_invite_page import MemberInvitePage
        save_locator = (MobileBy.ID, "com.tencent.wework:id/ie7")
        self.find_and_click(save_locator)
        return MemberInvitePage(self.driver)