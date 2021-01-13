
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.wait import WebDriverWait


class TestAddContect:

    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.WwMainActivity'
        caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_contact(self):
        locator = (MobileBy.XPATH, '//*[@text="通讯录"]')
        WebDriverWait(self.driver, 20).until(E.visibility_of_element_located(locator))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b78" and @text="必填"]').send_keys("乔峰")
        self.driver.find_elements(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b8_"]')[0].click()
        self.driver.find_elements(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bgf"]')[0].click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys("13845678888")
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b78" and @text="选填"]').send_keys("77896389@qq.com")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="设置部门"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Owen club"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="天龙八部"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gzz').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ie7').click()
        # 定位toast
        toast = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "添加成功")]').text
        assert toast == "添加成功"

