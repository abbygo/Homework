#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_qiyeweixin.page.base_page import BasePage
from appium_qiyeweixin.page.edit_member import EditMember


class SetMemberInfo(BasePage):
    '''
    设置成员信息
    '''
    def click_edit_member(self):
        # 点击个人信息页面编辑成员的图标
        el3 = self.find(MobileBy.ID, "com.tencent.wework:id/azn")
        el3.click()
        return EditMember(self._driver)
