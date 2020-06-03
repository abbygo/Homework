#abby
import os

from selenium_weixin.common.dir_config import page_path
from selenium_weixin.page.add_member import AddMember
from selenium_weixin.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    def goto_add_member(self):
        # 点击添加成员按钮
        self.steps(os.path.join(page_path, 'main.yaml'))
        return AddMember(self._driver)