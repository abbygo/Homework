# abby
import os

import pytest
import yaml

from selenium_weixin.common import dir_config
from selenium_weixin.page.index import Index


class TestRegister:
    def setup(self):
        self.index = Index()

    def teardown(self):
        pass

    @pytest.mark.parametrize('data', yaml.safe_load(
        open(os.path.join(dir_config.data_dir, 'test_register.yaml'), encoding='utf-8')))
    def test_register(self, data):
        self.index.goto_register().register(data['corp_name'], data['manager_name'], data['register_tel'])
