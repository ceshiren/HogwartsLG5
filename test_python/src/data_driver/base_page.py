from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import yaml

from test_python.src.data_driver.common.DecoratorXueqiu import black_list


class BasePage:
    def __init__(self, driver: webdriver = None):
        self.driver = driver

    @black_list
    def find(self, locator):
        return self.driver.find_element(*locator)

    def send(self, locator, key):
        return self.find(locator).send_keys(key)

    def find_and_click(self, locator):
        self.find(locator).click()

    def scroll_find_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find_and_click(element)

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def run_steps(self, path, operation):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        steps = data[operation]
        for step in steps:
            if step['action'] == "find_and_click":
                self.find_and_click(step['locator'])

            elif step['action'] == "send":
                # print(step['locator'], step['key'])
                self.send(step['locator'], step['key'])

            elif step['action'] == "scroll_find_click":
                self.scroll_find_click(step['locator'])

            elif step['action'] == "find_and_get_text":
                self.find_and_get_text(step['locator'])
