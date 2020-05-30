#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.member_invite import MemberInvite

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
