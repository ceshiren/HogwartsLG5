from selenium import webdriver


class BasePage:
    # _base_url = ""
    def __init__(self,driver:webdriver=None):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

        # if self._base_url != "":
        #     self.driver.get(self._base_url)

    def find(self,by,loc):
        return  self.driver.find_element(by,loc)