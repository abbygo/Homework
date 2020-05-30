#abby
import random

import pytest

from appium_xueqiu.page.app import App


class TestContact:

    def setup(self):
        self.app=App()
        print(self.app)
        self.main=self.app.start().main()

    def teardown_class(self):
       pass

    @pytest.mark.parametrize('name,phone', [('函数', random.randrange(18208120001, 19999999999))])
    def test_addcontact(self,name,phone):
        invitepage=self.main.goto_addresslist().add_member().\
            addmember_by_manul().input_name(name).set_gender().inputphonenum(phone).click_save()
        assert  '成功'  in invitepage.get_toast()
