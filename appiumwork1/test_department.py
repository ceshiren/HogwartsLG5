# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = "com.tencent.wework.launch.WwMainActivity"
        caps["noReset"] = "true"
        caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_demo(self):
        self.driver.find_element_by_id("com.tencent.wework:id/ie_").click()
        self.driver.find_element_by_id("com.tencent.wework:id/gwt").send_keys("july")
        sleep(1)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
        self.driver.find_element_by_id("com.tencent.wework:id/etm").send_keys("123")
        self.driver.find_element_by_id("com.tencent.wework:id/eti").click()

    @pytest.mark.skip
    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        result = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/pt").text
        assert result == "外出打卡成功"

    def test_add_member(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@resource-id,'com.tencent.wework:id/b78') and contains(@text,'必填')]").send_keys("可可")
        self.driver.find_element(MobileBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/"
                                 "android.widget.FrameLayout/"
                                 "android.widget.LinearLayout/"
                                 "android.widget.FrameLayout/"
                                 "android.widget.RelativeLayout/"
                                 "android.widget.ScrollView/"
                                 "android.widget.LinearLayout/"
                                 "android.widget.RelativeLayout[2]/"
                                 "android.widget.RelativeLayout/"
                                 "android.widget.RelativeLayout").click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fuy").send_keys("18855777090")
        self.driver.find_element(MobileBy.XPATH,'//*[@text="保存"]').click()
        result=self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"添加成功")]').text
        assert result == '添加成功'
