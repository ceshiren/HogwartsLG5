import time

from appium.webdriver.common.mobileby import MobileBy

from test_python.src.data_driver.common.DecoratorXueqiu import black_list
from test_python.src.data_driver.base_page import BasePage
from test_python.src.data_driver.pages.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.run_steps("../pages/main_page.yaml", "goto_market")
        return MarketPage(self.driver)

    def goto_mine(self):
        self.run_steps("../page/main_page.yaml", "goto_mine")
