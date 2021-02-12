import json
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def test_m():
    base = BasePage('')
    base.click_element_by(By.ID, 'menu_contacts')
    print('member_colLeft_top_addBtn')
    base.click_element_by(By.CLASS_NAME, "member_colLeft_top_addBtn")
    base.click_element_by(By.CSS_SELECTOR, "#js_contacts47 > div > div.member_colLeft > ul > li:nth-child(1) > a")
    base.send_keys_by(By.XPATH, "//form//input[1]", "技术部门")
    base.click_element_by(By.CLASS_NAME, "js_toggle_party_list")
    base.click_element_by(By.CLASS_NAME, "js_party_list_container")
    base.click_element_by(By.PARTIAL_LINK_TEXT, "确定")
    base.is_ele_exit(By.XPATH, "//ul[@class='jstree-children']")
    """//[@role=group]//li
    //*[@id="1688850237691796"]/ul //div[@class='datagrid-view1']/div[2]/div/table"
    """

    sleep(10)
    base.close()


class BasePage:
    def __init__(self, driver_arg: WebDriver = None):
        print('BasePage 的 init')
        ex_path = "C:\\Users\\zhangqin8909\\Desktop\\study\\hogwarts\\driver\\chromedriver.exe"
        if driver_arg is None:
            #     if browser == "firefox":
            #         self.driver = webdriver.Firefox(executable_path=ex_path)
            #     else:
            #         self.driver = webdriver.Chrome(executable_path=ex_path)
            self.driver = webdriver.Chrome(executable_path=ex_path)
            self._read_cookies('https://work.weixin.qq.com/wework_admin/frame#index')
            # self._write_cookies('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver_arg

    def _write_cookies(self, url):
        self._login_main(url)
        sleep(10)
        cookies = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

    def _read_cookies(self, url):
        self._login_main(url)
        with open("cookie.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def _login_main(self, url):
        self.driver.get(url)

    def click_element_by(self, by, element):
        self.driver.find_element(by, element).click()

    def is_ele_exit(self, by, element):
        try:
            self.driver.find_element(by, element)
        except NoSuchElementException as E:
            return False
        else:
            return True

    def send_keys_by(self, by, element, value):
        self.driver.find_element(by, element).send_keys(value)

    def close(self):
        self.driver.quit()
