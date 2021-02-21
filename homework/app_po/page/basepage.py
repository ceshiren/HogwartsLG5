from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_send_text(self, locator, text):
        self.find(locator).send_keys(text)

    def scroll_find_click(self, text):
        locator = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   f'scrollIntoView(new UiSelector().text("{text}").instance(0));')
        self.find_and_click(locator)

    def find_and_get_text(self, locator):
        return self.find(locator).text
