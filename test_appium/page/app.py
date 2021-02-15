
'''
1 打开app
2 重启app
3 关闭app
4 进入首页
'''
from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            des_caps = {
                'platformName': 'android',
                'platformVersion': '8.0.0',
                'appPackage': 'com.tencent.wework',
                'appActivity': 'com.tencent.wework.launch.LaunchSplashActivity',
                'noReset': 'true',
                'ensureWebviewHavaPages': True,
                'settings[waitForIdleTimeout]': 1
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", des_caps)
            self.driver.implicitly_wait(10)
            return self
        else:
            self.driver.launch_app()

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        pass

    def goto_main(self)->MainPage:
        return MainPage(self.driver)

