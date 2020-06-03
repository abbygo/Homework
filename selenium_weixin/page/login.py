#abby
from selenium_weixin.page.base_page import BasePage
from selenium_weixin.page.register import Register


class Login(BasePage):
    # 扫描登录
    def scanf(self):
        pass
    def goto_register(self):
        # click register
        # '.login_registerBar_link'
        return Register(self._driver)

