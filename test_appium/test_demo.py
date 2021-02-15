from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        des_caps = {
            'platformName' : 'android',
            'platformVersion' : '8.0.0',
            'appPackage' : 'com.tencent.wework',
            'appActivity' : 'com.tencent.wework.launch.LaunchSplashActivity',
            'noReset' : 'true',
            'ensureWebviewHavaPages': True,
            'settings[waitForIdleTimeout]' : 0
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        content = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/pu").text
        assert  content == "外出打卡成功"