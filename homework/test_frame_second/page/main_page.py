from homework.test_frame_second.basepage import BasePage
from homework.test_frame_second.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.run_steps("../yaml/main_page.yaml", 'goto_market_page')
        # self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        # self.find_and_click((MobileBy.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)
