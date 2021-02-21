import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from homework.test_frame.handle_black import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 把黑名单的判断抽离出来
    @handle_black
    def find(self, locator):
        return self.driver.find_element(*locator)
        # 先定义黑名单信息-locator列表
        # black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
        # try:
            # 如果找到元素直接返回
            # result = self.driver.find_element(*locator)
            # return result
        # 如果没有找到，执行except后的代码
        # except Exception as e:
            # 循环遍历黑名单列表，如果存在，那么对黑名单元素进行处理：点击关闭弹窗
            # for black in black_list:
            #     eles = self.driver.find_elements(*black)
            #     if len(eles) > 0:
            #         eles[0].click()
                # 处理黑名单后再次查找
                # return self.find(locator)
            # raise e

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

    def run_steps(self, file_path, operation):
        with open(file_path, 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
        steps = data[operation]
        for step in steps:
            action = step['action']
            if action == "find_and_click":
                self.find_and_click(step['locator'])
            elif action == "find_and_send_text":
                self.find_and_send_text(step['locator'], step['text'])
