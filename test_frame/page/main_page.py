from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage
from test_frame.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)