from appium.webdriver.common.mobileby import MobileBy
from appiumpo.page.addresslist_page import AddresslistPage
from appiumpo.page.base_page import BasePage

#点击通讯录列表
class MainPage(BasePage):

    def click_addresslist(self):
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.find_and_click((MobileBy.XPATH,"//*[@text='通讯录']"))  #调用basepage里面的封装查找和点击
        return AddresslistPage(self.driver)