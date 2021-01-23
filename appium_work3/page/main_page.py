from appium_work3.page.base_page import BasePage
from appium_work3.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.steps('main_page.yaml','goto_market')
        return MarketPage(self._driver)