#abby
import os

from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_normal.common.dir_config import page_path
from appium_xueqiu_normal.page.base_page import BasePage
from appium_xueqiu_normal.page.first_page import FirstPage
from appium_xueqiu_normal.page.market import Market


class Main(BasePage):
    '''
    进入行情
    '''
    def goto_market(self):

        # self.find(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        self.steps(os.path.join(page_path,'main.yaml'))
        return Market(self._driver)
    '''
    进入雪球
    '''
    def goto_xueqiu(self):
        self.find(MobileBy.XPATH, "//*[@text='雪球']").click()
        return FirstPage(self._driver)
    '''
    进入交易
    '''
    def goto_change(self):
        self.find(MobileBy.XPATH, "//*[@text='交易']").click()
    '''
    进入我的
    '''
    def goto_profile(self):
        self.find(MobileBy.XPATH, "//*[@text='我的']").click()