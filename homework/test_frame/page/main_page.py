from appium.webdriver.common.mobileby import MobileBy

from homework.test_frame.basepage import BasePage
from homework.test_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        self.find_and_click((MobileBy.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)