# abby
import shelve

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

'''
复用cookies
'''
class TestCookie():
    def setup_method(self):
        options = Options()
        # 设置debug地址
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):

        # 一定要先访问，否则会报 invilde domain
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        with shelve.open('cookies/cookies') as db:
            # 空的时候，就添加字典的元素
            if db.get('cookie') is None:
                db['cookie'] = self.driver.get_cookies()

            cookies = db['cookie']
        # 循环加入cookie
        for cookie in cookies:
            # 处理掉不合法的参数
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            # 添加cookie
            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_xpath("//*[text()='通讯录']").click()
