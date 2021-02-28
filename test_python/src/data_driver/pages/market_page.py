from test_python.src.data_driver.base_page import BasePage
from test_python.src.data_driver.pages.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.run_steps("../pages/market_page.yaml", 'goto_search')
        return SearchPage(self.driver)