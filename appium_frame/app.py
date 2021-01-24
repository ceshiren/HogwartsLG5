from appium import webdriver

from appium_frame.base_page import BasePage
from appium_frame.page.main_page import MainPage


class App(BasePage):
    def start(self):
        #复用APP:当driver空的时候（首次跑APP的时候，driver会是空），就走if里面的脚本；如果不是为空就launch app，也就是去拿APP里面的信息来启动APP
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "雪球"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    #重启APP
    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    #关闭APP
    def stop(self):
        self.driver.quit()
        return self

    #进入主页
    def goto_main(self)->MainPage:
        return MainPage(self.driver)
