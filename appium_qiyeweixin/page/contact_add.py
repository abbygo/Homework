#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_qiyeweixin.page.base_page import BasePage

'''
添加联系人页面
'''
class ContractAdd(BasePage):

    '''
    联系人添加
    '''
    def input_name(self,name):
        # 输入姓名

        self.find(MobileBy.XPATH, "//*[@text='姓名　']/..//*[@class='android.widget.EditText']").send_keys(
            name)

        return self

    def set_gender(self):
        # 点击出性别弹框
        self.find(MobileBy.XPATH, "//*[@text='男']").click()
        # 选择性别女
        self.find(MobileBy.XPATH, "//*[@text='女']").click()
        return self


    def inputphonenum(self,phone):
        # 输入手机号
        self.find(MobileBy.ID, "com.tencent.wework:id/er6").send_keys(phone)

        return self

    def click_save(self):
        #         点击保存
        self.find(MobileBy.ID, 'com.tencent.wework:id/gvy').click()

        from appium_qiyeweixin.page.member_invite import MemberInvite
        return MemberInvite(self._driver)