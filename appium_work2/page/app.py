from appium import webdriver
from appium_work2.page.base_page import BasePage
from appium_work2.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "Mumu"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            # caps["skipDeviceInitialization"] = "true" #跳过安装、权限设置等操作
            # caps["dontStopAppOnReset"] = "true" #首次启动的时候，不停止app
            '''
            获取app的包名、activity
            mac：adb logcat "ActivityManager:I *:s" | grep "cmp"
            win：adb logcat ActivityManager:I *:s | findstr "cmp"
            '''
            caps["noReset"] = "true"  # 不清空本地缓存，启动app
            caps["ensureWebviewsHavePages"] = True
            caps['settings[waitForIdleTimeout]'] = 1  # 设置页面等待空闲状态的时间为0秒
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self)->MainPage:
        return MainPage(self.driver)