#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.contact_add import ContractAdd

'''
添加成员方式列表页面
'''
class MemberInvite(BasePage):
    '''
    手动添加成员
    '''
    def addmember_by_manul(self):
        self.find(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        return ContractAdd(self._driver)

    def get_toast(self):
        import time
        time.sleep(1)
        return self.find_and_get_text(MobileBy.XPATH, "//*[@class='android.widget.Toast']")

