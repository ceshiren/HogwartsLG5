"""
__author__ = 'jaxon'
__time__ = '2021/1/16 下午9:06'
__desc__ = ''
"""
#
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from test_frame.handle_black import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def send(self, locator, content):
        self.find(locator).send_keys(content)

    def scroll_find_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find_and_click(element)

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def run_steps(self, page_path, operation):
        # yaml 的读取
        with open(page_path, 'r', encoding="utf-8") as f:
            data = yaml.load(f)
        # 支持 PO 下多个操作
        steps = data[operation]
        # 遍历每一个动作
        for step in steps:
            action = step['action']
            # 如果动作是 find_and_click ，就调用 basepage 中的 find_and_click
            if action == "find_and_click":
                # 调用 find_and_click 并且传入相应参数
                self.find_and_click(step['locator'])
            elif action == "send":
                self.send(step['locator'], step['content'])