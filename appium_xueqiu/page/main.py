#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.addresslist_page import AddressList
from appium_xueqiu.page.base_page import BasePage


class Main(BasePage):
    '''
    进入消息页面
    '''
    def goto_message(self):
        pass
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