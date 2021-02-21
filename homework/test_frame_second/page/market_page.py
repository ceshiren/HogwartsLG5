from appium.webdriver.common.mobileby import MobileBy

from homework.test_frame_second.basepage import BasePage
from homework.test_frame_second.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.run_steps("../yaml/market_page.yaml", "goto_search")
        # self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)
