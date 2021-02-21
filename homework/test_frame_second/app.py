# 启动app，关闭app，重启app，进入首页等操作
from appium import webdriver


from homework.test_frame_second.basepage import BasePage
from homework.test_frame_second.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            # 雪球app的包名和活动名
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".common.MainActivity"
            # 企业微信app的包名和活动页面名称信息
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.WwMainActivity"
            # 不清空本地缓存，启动app
            caps["noReset"] = "true"
            # caps["unicodeKeyBoard"] = "true"
            # caps["resetKeyBoard"] = "true"
            # caps["ensureWebviewsHavePages"] = True
            # 不关闭app
            # caps["dontStopAppOnReset"] = "true"
            # 设置页面等待空闲状态的时间为0秒
            caps['settings[waitForIdleTimeout]'] = 1
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def goto_main(self):
        return MainPage(self.driver)
