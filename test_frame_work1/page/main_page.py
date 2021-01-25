from appium.webdriver.common.mobileby import MobileBy
from test_frame_work1.base.base_action import BaseAction
from test_frame_work1.page.markey_page import MarketPage


class MainPage(BaseAction):
    def goto_market_page(self):
        self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        self.find_and_click((MobileBy.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)