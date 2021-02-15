from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage


class ContactEditPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def edit_name(self,name):
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[@resource-id='com.tencent.wework:id/b7m' and @text='必填']").send_keys(name)
        self.find_and_text((MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/b7m' and @text='必填']"),name)
        return self

    def edit_gender(self,gender):
        locator = (MobileBy.XPATH, "//*[@text='男']")
        ele = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        if gender == "女":
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        else:
            self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        return self

    def edit_phone(self,phonenum):
        self.find_and_text((MobileBy.ID, 'com.tencent.wework:id/fwi'),phonenum)
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fwi').send_keys(phonenum)
        return self

    def click_save(self):
        self.scroll_and_find("保存后自动发送邀请通知")
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("保存后自动发送邀请通知").instance(0));')
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/aja"))
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/aja").click()
        return self

    def get_toast(self):
        toast_content = self.get_toast_content()
        # toast_content = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_content
