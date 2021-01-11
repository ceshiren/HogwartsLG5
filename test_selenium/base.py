from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.drive.maximize_window()#游览器最大化
        self.driver.implicitly_wait(5)#隐式等待5s 及等加载完或等待满5s

    def teardown(self):
        self.driver.quit()