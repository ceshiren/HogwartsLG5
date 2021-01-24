from selenium.webdriver.common.by import By

from appium_frame.base_page import BasePage
from appium_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        #点击行情时出现的弹窗或者黑名单--例：发表评论弹窗
        self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        #点击行情tab
        self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)