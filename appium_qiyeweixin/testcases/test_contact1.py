# abby
import random

import pytest

from appium_qiyeweixin.common.constant import Constant
from appium_qiyeweixin.page.app import App
from appium_qiyeweixin.page.main import Main
from appium_qiyeweixin.page.member_invite import MemberInvite


class TestContact:

    def setup_class(self):
        self.app = App()

        self.main = self.app.start().main()
        self.dirver = getattr(Constant, 'driver')

    def teardown(self):


        #
        Main(self.dirver).goto_message()

    @pytest.mark.parametrize('name,phone', [('函数', random.randrange(18208120001, 19999999999)),('文章', random.randrange(17208120001, 17999999999))])
    def test_addcontact(self, name, phone):

        invitepage = self.main.goto_addresslist().add_member(). \
            addmember_by_manul().input_name(name).set_gender().inputphonenum(phone).click_save()
        assert '成功' in invitepage.get_toast()
        MemberInvite(self.dirver).back_address_list()

    def test_delcotact(self):
        self.main.goto_addresslist().click_member().\
            goto_edit_member().click_edit_member().del_member()
