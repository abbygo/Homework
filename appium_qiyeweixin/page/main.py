#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_qiyeweixin.page.addresslist_page import AddressList
from appium_qiyeweixin.page.base_page import BasePage
from appium_qiyeweixin.page.message_list import MessageList


class Main(BasePage):
    '''
    进入消息页面
    '''
    def goto_message(self):
        self.find(MobileBy.XPATH, "//*[@text='消息']").click()
        return MessageList(self._driver)
    '''
    进入通讯录
    '''
    def goto_addresslist(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressList(self._driver)
    '''
    进入工作台
    '''
    def goto_workbench(self):
        pass
    '''
    进入我的
    '''
    def goto_profile(self):
        pass