from base_page import BasePage

class AddMember(BasePage):
    _name_loc =('xpath','//android.widget.ScrollView[@resource-id="com.tencent.wework:id/bck"]//android.widget.RelativeLayout[@resource-id="com.tencent.wework:id/ern"]//android.widget.EditText[@resource-id="com.tencent.wework:id/b78"]')#姓名
    _sex_loc = ('xpath','//*[@text="男"]')#性别选项
    _sex0_loc = ('xpath','//*[@text="男"]/../..//*[@resource-id="com.tencent.wework:id/elq"]')#性别男
    _sex1_loc = ('xpath','//*[@text="女"]/../..//*[@resource-id="com.tencent.wework:id/elq"]')#性别女
    _phone_loc = ('id','com.tencent.wework:id/fuy')#手机号
    _save_loc = ('id','com.tencent.wework:id/ie7')#保存

    def send_name(self,name):
        '''输入姓名'''
        self.sendkeys(self._name_loc,name)
        return self

    def choice_sex(self,sex):
        '''选择性别，默认选男'''
        self.clicks(self._sex_loc)
        if sex == '男':
            self.clicks(self._sex0_loc)
        elif sex == '女':
            self.clicks(self._sex1_loc)
        else:
            self.clicks(self._sex0_loc)
        return self

    def send_phone(self,phone):
        '''输入手机号'''
        self.send(self._phone_loc,phone)
        return self

    def click_save(self):
        '''点击保存'''
        self.clicks(self._save_loc)
        from add_member_choice_page import AddMemberChoice
        return AddMemberChoice(self._driver)