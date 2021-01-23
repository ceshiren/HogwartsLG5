import yaml
from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.run_steps("../page/market_page.yaml", "goto_search")
        # self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)