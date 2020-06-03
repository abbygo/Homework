#abby
import os

from selenium_weixin.common.dir_config import page_path
from selenium_weixin.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self,**kwargs):
        # 将传入的dict更新到 _params
        self._params.update(kwargs)

        self.steps(os.path.join(page_path, 'add_member.yaml'))
        return self

    def delete_member(self):
        # //span[text()="德克士"]/../../td[1]
        self.steps(os.path.join(page_path, 'add_member.yaml'))


    def update_page(self):
    #     获取页码文本

        pass


    def get_member(self):
        '''
        获取成员信息
        :return: True 或者False
        '''
        # '.member_colRight_memberTable_td:nth-child(2)'
        # for ele in elemets:
        #     if value==ele.get_attribute("title"):
        #         return True
        #
        # return False
        return self.steps(os.path.join(page_path, 'add_member.yaml'))
