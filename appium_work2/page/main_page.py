from appium_work2.page.base_page import BasePage
from appium_work2.page.market_page import MarketPage


class MainPage(BasePage):
    _market_loc = ('xpath','//*[@text="行情"]')#行情
    _cont_loc = ('xpath',"//*[@resource-id='com.xueqiu.android:id/post_status']")#发稿
    def goto_market(self):
        self.click_new(self._cont_loc)#点击发稿
        self.click_new(self._market_loc)#点击行情
        return MarketPage(self._driver)