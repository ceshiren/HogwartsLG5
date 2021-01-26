import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddmember():
    def setup_class(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "127.0.0.1:21503",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.LaunchSplashActivity",
            "noReset": "true",
            "automationName":"uiautomator2"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
    def teardown_class(self):
        self.driver.quit()
    def test_addmember(self):
        name = "WG"
        tel = "12312312320"
        gender = "男"
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员"))').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/b8_']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys(tel)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        toast = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "添加成功")]').text
        assert "添加成功" == toast

if __name__=="__main__":
    pytest.main([])