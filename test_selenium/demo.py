from selenium import webdriver
class Test_selenium:
    def setup_class(self):
        self.drive = webdriver.Chrome()
        self.drive.maximize_window()#游览器最大化
        self.drive.implicitly_wait(5)#隐式等待5s 及等加载完或等待满5s

    def teardown_class(self):
        self.drive.quit()