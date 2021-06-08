from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddContact:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.run(order = 2)
    def test_add_contact(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                 'scrollable(true).instance(0)).'
                                                 'scrollIntoView(new UiSelector().text("添加成员"))').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys('王二y')
        self.driver.find_element(MobileBy.XPATH, '//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/aub"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b9z"]//*[@text="男"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/eq7').send_keys('15300052204')
        self.driver.find_element(MobileBy.XPATH, '//*[@text="地址"]/..//*[@resource-id="com.tencent.wework:id/aub"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gz').send_keys('杭州')
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gur" and @text="确定"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gur" and @text="保存"]').click()
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,"")))
        res = self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text
        assert "添加成功" == res