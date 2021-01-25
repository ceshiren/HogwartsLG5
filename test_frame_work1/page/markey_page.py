from appium.webdriver.common.mobileby import MobileBy
from test_frame_work1.base.base_action import BaseAction
from test_frame_work1.page.search_page import SearchPage


class MarketPage(BaseAction):
    def goto_search(self):
        self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)