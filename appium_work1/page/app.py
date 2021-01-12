import yaml
from appium import webdriver
from base_page import BasePage
from appium_work1.page.main import Main


class App(BasePage):

    def start(self,path='../config/app.yaml'):
        res = self.open_yaml(path)
        if self._driver == None:
            try:
                print('无driver，启动driver')
                capability_conf = {}
                capability_conf['platformName'] = res['platformName']
                capability_conf['deviceName'] = res['deviceName']
                capability_conf['appPackage'] = res['appPackage']
                capability_conf['appActivity'] = res['appActivity']
                capability_conf['noReset'] = res['noReset']
                capability_conf['unicodeKeyboard'] = res['unicodeKeyboard']
                capability_conf['resetKeyboard'] = res['resetKeyboard']
                capability_conf['chromedriverExecutableDir'] = res['chromedriverExecutableDir']
                # capability_conf['dontStopAppOnReset'] = res['dontStopAppOnReset']
                self._driver = webdriver.Remote(res['ip'] + res['host'], capability_conf)
                print(f'当前连接的设备信息为：{capability_conf}')
                self._driver.implicitly_wait(3)
            except Exception as e:
                raise e
        else:
            print('有driver,加载包名')
            self._driver.start_activity(res['appPackage'], res['appActivity'])
        return self

    def main(self)->Main:
        return Main(self._driver)

if __name__ == '__main__':
    pass