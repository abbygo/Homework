# abby
import os

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_normal.common.dir_config import data_dir
from appium_xueqiu_normal.page.app import App


class TestSearch:

    def setup_class(self):
        self.search = App().start().main().goto_market().goto_search()

    def teardown(self):
        self.search.back_market()

    def teardown_class(self):
        App().stop()


    @pytest.mark.parametrize('data',
                             yaml.safe_load(open(os.path.join(data_dir, 'test_search.yaml'), encoding='utf-8')))
    def test_search(self, data):
        self.search.search(data['searchkey'], data['search_result']).add(data['search_result'])
        assert self.search.is_choose(data['search_result'])
        self.search.reset(data['search_result'])
