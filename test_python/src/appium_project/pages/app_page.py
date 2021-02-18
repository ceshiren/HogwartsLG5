import os
import sys

import yaml
from appium import webdriver
from test_python.src.appium_project.pages.base_page import BasePage
from test_python.src.appium_project.pages.main_page import MainPage


class AppPage(BasePage):
    def start(self):
        if self.driver == None:
            self.driver = self.read_capbilities()
        else:
            self.driver.launch_app()
        return self

    def read_capbilities(self):
        path = os.path.dirname(__file__).strip("pages").__add__("datas/capbilities.yaml")
        print(path)
        with open(path, 'r') as f:
            data = yaml.load(f)

            desired_caps = {'platformName': data['platformName'], 'platformVersion': data['platformVersion'],
                            'deviceName': data['deviceName'], 'app': data['app'], 'appPackage': data['appPackage'],
                            'appActivity': data['appActivity'], 'noReset': data['noReset'],
                            'automationName': data['unicodeKeyboard']}

        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
        driver.implicitly_wait(8)
        return driver

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self) -> MainPage:

        return MainPage(self.driver)
