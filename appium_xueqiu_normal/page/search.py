#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_normal.page.base_page import BasePage


class Search(BasePage):
    def search(self,searchkey,search_result):



        # 点击搜索按钮
        el73 = self.find(MobileBy.ID, "com.xueqiu.android:id/action_search").click()
        # 输入搜索内容
        el3 = self.find(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        # 点击搜索的下拉框
        el4 = self.find(MobileBy.XPATH, f"//*[@text='{search_result}']")
        el4.click()
        return self

    def add(self,search_result):
        '''
        添加股票
        :param search_result:
        :return:
        '''
        el5 = self.finds(MobileBy.XPATH, f"//*[@text='{search_result}']/../../..//*[@text='加自选']")

        if len(el5) > 0:

            el5[0].click()
        return self

    def is_choose(self,search_result):
        '''
        重置环境
        :param search_result:
        :return:
        '''
        el5 = self.finds(MobileBy.XPATH, f"//*[@text='{search_result}']/../../..//*[@text='已添加']")

        if len(el5) > 0:
            return el5

    def rest(self,search_result):
        '''
        重置环境
        :param search_result:
        :return:
        '''
        el5 = self.finds(MobileBy.XPATH, f"//*[@text='{search_result}']/../../..//*[@text='已添加']")

        if len(el5) > 0:
            el5[0].click()
        return self

    def back_market(self):
        self.find(MobileBy.ID, "com.xueqiu.android:id/action_close").click()