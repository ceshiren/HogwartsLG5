from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from appium_frame.handle_black import handle_black

#初始化driver
class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    #封装查找元素
    @handle_black
    def find(self,loc):
        return self.driver.find_element(*loc)

    #封装查找元素和点击
    def find_and_click(self,locator):
        self.find(locator).click()

    def send(self,locator,value):
        self.find(locator).send_keys(value)

    #封装滑动查找和点击,调用text的值，ele等于text的值
    def scroll_find_click(self,text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));')
        self.find_and_click(element)

    #封装toast值
    def find_and_get_text(self,result):
        return self.find(result).text



