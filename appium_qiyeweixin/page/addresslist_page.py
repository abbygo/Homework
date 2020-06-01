#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_qiyeweixin.page.base_page import BasePage
from appium_qiyeweixin.page.member_info import MemberInfo
from appium_qiyeweixin.page.member_invite import MemberInvite

'''
通讯录页面
'''

class AddressList(BasePage):
    '''
    添加成员
    '''
    def add_member(self):
        self.scroll_ele_and_click('添加成员')
        # self.find(MobileBy.XPATH,"//*[@text='添加成员']").click()

        return MemberInvite(self._driver)

    def click_member(self):
        # 点击成员
        self.scroll_ele_and_click('企业通讯录',click=False)
        el1 =self.find(MobileBy.XPATH,"//*[@text='企业通讯录']/..")
        el1.click()
        return MemberInfo(self._driver)

