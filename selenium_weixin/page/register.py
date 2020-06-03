#abby
import os

from selenium_weixin.common.dir_config import page_path
from selenium_weixin.page.base_page import BasePage


class Register(BasePage):
    def register(self,corp_name,manager_name,register_tel):
       # 企业名称
       # '#corp_name'
       # 选择行业类型
       # '//*[text()="选择行业类型"]'
       #
       self._params['corp_name']=corp_name
       self._params['manager_name'] = manager_name
       self._params['register_tel'] = register_tel
       self.steps(os.path.join(page_path, 'register.yaml'))
       return True