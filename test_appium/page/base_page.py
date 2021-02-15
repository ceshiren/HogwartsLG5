from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find(self,locator):
        return self.driver.find_element(*locator)

    def find_and_click(self,locator):
        ele = self.find(locator)
        ele.click()

    def find_and_text(self,locator,text):
        ele = self.find(locator)
        ele.send_keys(text)

    def find_and_get_text(self,locator):
        #获取文本信息
        return self.find(locator).text

    def scroll_and_find(self,text):
        #滑动并查找到元素
        ele =(MobileBy.ANDROID_UIAUTOMATOR,
             'new UiScrollable(new UiSelector().'
             'scrollable(true).instance(0)).'
             'scrollIntoView(new UiSelector().'
             f'text("{text}").instance(0));')
        return self.find(ele)

    def scroll_and_find_and_click(self,text):
        #滑动查找到元素后，点击元素
        self.scroll_and_find(text).click()

    def get_toast_content(self):
        toast = self.find((MobileBy.XPATH, "//*[@class='android.widget.Toast']")).text
        return toast


