#abby
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class TestSearch:
    def setup_class(self):

        caps={
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "Android Emulator",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": "true",
            "noReset": "true"
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    def teardown(self):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/action_close").click()
    @pytest.mark.parametrize('searchkey,search_result',[('alibaba','阿里巴巴'),('jd','京东')])
    def test_search(self,searchkey,search_result):
        el2 = self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
        el3 = self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        # 点击搜索的下拉框
        el4 = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{search_result}']")
        el4.click()
        el5 = self.driver.find_elements(MobileBy.XPATH,f"//*[@text='{search_result}']/../../..//*[@text='加自选']")

        if len(el5)>0:

            el5[0].click()
        else:
            pass


