#abby
from appium.webdriver.common.mobileby import MobileBy
from appium_qiyeweixin.page.base_page import BasePage

class EditMember(BasePage):
    def del_member(self):
        # 点击个人信息页面编辑成员页面的删除成员按钮
        el4 = self.find(MobileBy.ID, "com.tencent.wework:id/dvn")
        el4.click()
        # 点击弹出框上的确认删除按钮
        el5 = self.find(MobileBy.ID, "com.tencent.wework:id/b_d")
        el5.click()
        from appium_qiyeweixin.page.addresslist_page import AddressList
        return AddressList(self._driver)