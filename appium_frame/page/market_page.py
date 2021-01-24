from selenium.webdriver.common.by import By
from appium_frame.base_page import BasePage
from appium_frame.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        #点击搜索
        self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)