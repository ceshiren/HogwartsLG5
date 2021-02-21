from appium.webdriver.common.mobileby import MobileBy

from homework.test_frame.basepage import BasePage


class SearchPage(BasePage):
    def search(self):
        self.find_and_send_text((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']"), "alibaba")