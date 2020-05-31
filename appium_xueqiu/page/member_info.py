#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.set_memberinfo import SetMemberInfo


class MemberInfo(BasePage):
    '''
    成员详情页面
    '''

    def goto_edit_member(self):
        # 点击个人信息页面右上角的图标
        el2 = self.find(MobileBy.ID, "com.tencent.wework:id/gvr")
        el2.click()
        return SetMemberInfo(self._driver)
