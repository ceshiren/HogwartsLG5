from selenium.webdriver.common.by import By
from appium_frame.base_page import BasePage


class SearchPage(BasePage):
    #定义搜索页面
    def search(self):
        self.send((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']"),"阿里巴巴")
        self.find_and_click((By.XPATH,'//*[@text="阿里巴巴-SW"]'))
        return True