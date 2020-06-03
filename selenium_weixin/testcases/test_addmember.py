#abby
import os

import pytest
import yaml

from selenium_weixin.common import dir_config
from selenium_weixin.page.main import Main


class TestAddMember():
    def setup(self):
        self.main=Main()
    def teardown(self):
        self.add_member.delete_member()
    @pytest.mark.parametrize('data',yaml.safe_load(open(os.path.join(dir_config.data_dir,'test_addmember.yaml'),encoding='utf-8')))
    def test_add_member(self,data):
        self.add_member=self.main.goto_add_member()
        self.add_member.add_member(**data)
        assert self.add_member.get_member()

