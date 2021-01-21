from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appiumpo.page.base_page import BasePage

#联系人编辑页面，输入姓名、性别、电话号码以及保存，再返回到邀请成员列表页
class ContactEditPage(BasePage):
    def edit_name(self,name):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@resource-id,'com.tencent.wework:id/b78') and contains(@text,'必填')]").send_keys(
            name)
        return self

    def edit_gender(self,gender):
        #当运行脚本时，提示dom里找不到元素时，可能是页面加载时查找元素找不到，可使用显示等待，等页面全部加载出来的时候再去找元素
        locator = MobileBy.XPATH, '//*[@text="男"]'
        element = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))   #再一定时间内找到元素是否可点击
        element.click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        if gender == '女':
            # self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
            self.find_and_click((MobileBy.XPATH, '//*[@text="女"]'))
        else:
            # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
            self.find_and_click((MobileBy.XPATH, '//*[@text="男"]'))
        return self

    def edit_phone(self,phone):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys(phone)
        return self

    def click_save(self):
        from appiumpo.page.memberinvite_page import MemberinvitePage
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        self.find_and_click((MobileBy.XPATH, '//*[@text="保存"]'))
        return MemberinvitePage(self.driver)