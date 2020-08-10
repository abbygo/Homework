#abby
import os

from appium import webdriver
from selenium.webdriver.common import utils

from appium_xueqiu_normal.common.constant import Constant
from appium_xueqiu_normal.page.base_page import BasePage
from appium_xueqiu_normal.page.main import Main


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
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "autoGrantPermissions": "true",
                "noReset": "true",
                "skipServerInstallation":"true",
                "skipDeviceInitialization": "true",
                "newCommandTimeout":"180"
            }

            caps['udid'] = os.getenv('udid', None)
            # forward 的端口会冲突
            caps['systemPort']=utils.free_port()
            caps['mjpegServerPort']=utils.free_port()
            # caps['chromedriverPort']=utils.free_port()
            print('------------------------------')
            print(caps['udid'] )
            print(caps['systemPort'])
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
        driver=getattr(Constant,'driver')

        driver.quit()

    '''
       进入主页
    '''
    def main(self)->Main:

        return Main(self._driver)