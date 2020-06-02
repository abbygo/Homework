#abby
import shelve

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import  webdriver

'''
复用浏览器
'''
class TestDemo():
    def setup_method(self):
        options=Options()
        # 前置条件是 cmd  开启了:chrome --remote-debugging-port=9222
        # 设置debug地址
        options.debugger_address='127.0.0.1:9222'
        self.driver=webdriver.Chrome(options=options)


    def teardown(self):
        self.driver.quit()


    def test_repeat_use_browser(self):
        # 在debug 的浏览器中 已经登录了需要测试的网页
        self.driver.find_element_by_xpath("//*[text()='通讯录']").click()
        import time
        time.sleep(3)

