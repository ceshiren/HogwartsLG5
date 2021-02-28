from test_python.src.appium_frame.base_page import BasePage
from test_python.src.data_driver.pages.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):

        return SearchPage(self.driver)