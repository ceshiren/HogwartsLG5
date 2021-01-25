import pytest
from appium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_CreateNewMember:
    def setup_method(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        caps["unicodeKeyBoard"] = "true"
        caps["resetKeyBoard"] = "true"
        caps["ensureWebviewsHavePages"] = True
        caps["dontStopAppOnReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().'
            'scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().'
            'text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]").click()
        text = self.driver.find_element_by_id("com.tencent.wework:id/pt").text
        assert text == "外出打卡成功"
        # 返回到主页-消息页
        self.driver.back()
        self.driver.find_element_by_xpath("//*[@text='消息']").click()


    def test_createnewmember(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        # self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        # 将添加成员改成滑动定位
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().'
            'scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().'
            'text("添加成员").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        # 填写新增成员信息:名字
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("李四")
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/../android.widget.RelativeLayout").click()
        sleep(1)
        # 选择性别
        self.driver.find_element_by_xpath("//*[@text='男']").click()
        # 手机号
        self.driver.find_element_by_xpath("//*[@text='手机号']").send_keys("11111111111")
        # 邮箱
        self.driver.find_element_by_xpath("//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys("lisi@qq.com")
        # 地址
        self.driver.find_element_by_xpath("//*[contains(@text,'地址')]/../android.widget.RelativeLayout").click()
        self.driver.find_element_by_id("com.tencent.wework:id/js").send_keys("腾讯大厦")
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/ejm']/android.widget.RelativeLayout[1]").click()
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        # 保存新增成员
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        # 判断成员是否添加成功
        ele = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert ele == "添加成功"

