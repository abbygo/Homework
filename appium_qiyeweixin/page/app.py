#abby
import os

from appium import webdriver

from appium_qiyeweixin.common.constant import Constant
from appium_qiyeweixin.page.base_page import BasePage
from appium_qiyeweixin.page.main import Main


class App(BasePage):
    '''
    管理app
    '''
    '''
    启动appp，
    '''
    def start(self):
        if self._driver is None:
            caps = {
                "platformName": "Android",
                "deviceName": "Android Emulator",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "autoGrantPermissions": "true",
                "noReset": "true",
                "skipServerInstallation":"true",
                "skipDeviceInitialization": "true"
            }
            udid=os.getenv('UDID',None)
            if udid!=None:
                caps['udid']=udid
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            setattr(Constant,'driver',self._driver)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self
    '''
    重启app
    '''
    def restart(self):
        pass

    '''
       停止app
    '''
    def stop(self):
        if self._driver:

            self._driver.quit()

    '''
       进入主页
    '''
    def main(self)->Main:

        return Main(self._driver)