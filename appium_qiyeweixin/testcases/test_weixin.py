#abby
import random

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class TestWeixin:
    def setup_class(self):

        caps={
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "Android Emulator",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "autoGrantPermissions": "true",
            "noReset": "true"
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()


    def teardown(self):
        pass


    @pytest.mark.parametrize('name,phone',[('函数',random.randrange(18208120001,19999999999))])
    def test_addcontact(self,name,phone):
        '''
        添加联系人
        :param name: 姓名
        :param phone: 电话
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        # 输入姓名
        self.driver.find_element(MobileBy.XPATH,"//*[@text='姓名　']/..//*[@class='android.widget.EditText']").send_keys(name)
        # 点击出性别弹框
        self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        # 选择性别女
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # 输入手机号
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/er6").send_keys(phone)
#         点击保存
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/gvy').click()
        import time
        time.sleep(1)
        success_msg=self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成功']").text
        assert success_msg in '添加成功'


