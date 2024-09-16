import json

import pytest
from selenium import webdriver


class WechatCom:
    def setup_class(self):
        print("=====================开始============================")
        driver_path = "C:\\Users\\zhangqin8909\\Desktop\\study\\hogwarts\\driver\\chromedriver.exe"
        options_args = webdriver.ChromeOptions()
        options_args.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options_args, executable_path=driver_path)
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()
        with open("./cookie.json", "r") as f:
            cookies = json.load(f)
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def teardown_method(self):
        self.driver.quit()
        print("=====================结束============================")
