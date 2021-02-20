import time

from appium.webdriver.common.mobileby import MobileBy

from test_python.src.appium_frame.common.decorator_xueqiu import black_list
from test_python.src.appium_frame.pages.base_page import BasePage
from test_python.src.appium_frame.pages.contact_page import ContactPage


class MainPage(BasePage):
    @black_list
    def goto_market(self):
        self.find((MobileBy.XPATH, "//*[@text='行情']")).click()
        time.sleep(3)
        return True
