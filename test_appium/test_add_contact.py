from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddContact:
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

    def test_add_contact(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/cth").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/b7m' and @text='必填']").send_keys("张三")
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/fwi').send_keys("13101018813")
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("保存后自动发送邀请通知").instance(0));').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/aja").click()
        toast_content = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        assert toast_content == "添加成功"

