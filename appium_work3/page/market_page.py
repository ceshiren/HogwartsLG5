from appium_work3.page.base_page import BasePage
from appium_work3.page.search_page import SearchPage


class MarketPage(BasePage):

    def goto_search(self):
        self.steps('market_page.yaml','goto_search')
        return SearchPage(self._driver)
