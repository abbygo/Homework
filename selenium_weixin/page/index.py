#abby
import os

from selenium_weixin.common.dir_config import page_path
from selenium_weixin.page.base_page import BasePage
from selenium_weixin.page.login import Login
from selenium_weixin.page.register import Register


class Index(BasePage):
    _base_url='https://work.weixin.qq.com/'
    def goto_login(self):
        # 点击登录按钮
        # '.index_top_operation_loginBtn'
        self.steps(os.path.join(page_path, 'index.yaml'))
        return Login(self._driver)
    def goto_register(self):
        # 点击注册按钮
        # '.index_head_info_pCDownloadBtn'
        self.steps(os.path.join(page_path, 'index.yaml'))
        return Register(self._driver)