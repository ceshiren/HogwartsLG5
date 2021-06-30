from test_frame.basepage import BasePage
from test_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.run_steps("../page/main_page.yaml", "goto_market_page")
        # self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        # self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)

    def goto_mine(self):
        self.run_steps("../page/main_page.yaml", "goto_mine")