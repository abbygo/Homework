#abby
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_normal.page.app import App


class TestSearch:

    def setup_class(self):
        self.search=App().start().main().goto_market().goto_search()

    def teardown(self):
        self.search.back_market()
    def teardown_class(self):
        App().stop()

    @pytest.mark.parametrize('searchkey,search_result',[('alibaba','阿里巴巴'),('jd','京东')])
    def test_search(self,searchkey,search_result):
        self.search.search(searchkey,search_result).add(search_result)
        assert self.search.is_choose(search_result)
        self.search.rest(search_result)



