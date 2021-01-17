from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Mumu"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        '''
        获取app的包名、activity
        mac：adb logcat "ActivityManager:I *:s" | grep "cmp"
        win：adb logcat ActivityManager:I *:s | findstr "cmp"
        '''
        caps["noReset"] = "true"  # 不清空本地缓存，启动app
        caps["ensureWebviewsHavePages"] = True
        caps['settings[waitForIdleTimeout]'] = 0  # 设置页面等待空闲状态的时间为0秒
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    '''
    常用定位
    //*[contains(@resource-id, ‘login’)]（重点）
    //*[@text=‘登录’]  （重点）
    //*[contains(@resource-id, ‘login’) and contains(@text, ‘登录’)] （重点）
    '''

    def test_add_member(self):
        name = '测试帐号1'
        gender = '男'
        phonenum = '17100000001'
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@resource-id, "com.tencent.wework:id/elq") and '
                                                 'contains(@text, "通讯录")]').click()  # 使用组合定位，避免页面中其他带通讯录的元素干扰
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,  # 添加成员按钮不在第一屏时，滑动查找，实际使用中复制即可
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        locator = (MobileBy.XPATH, "//*[@text='男']")
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        ele.click()
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys(phonenum)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        ToastText = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "添加成功" == ToastText
