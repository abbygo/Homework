#abby
import logging

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By



class BasePage():
    # 黑名单列表
    _back_list=[
        (By.XPATH,"//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),

    ]
    # 错误次数
    _error_num=0
    # 最大错误次数
    _max_num=3
    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    def find(self,locator,value:str=None):
        logging.info(locator)
        logging.info(value)
        try:
            element:WebElement
            if isinstance(locator,tuple):
                element=self._driver.find_element(*locator)
            else:
                element=self._driver.find_element(locator,value)
            self._error_num=0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            # 异常情况，需要调整等待时间，优化处理弹框的速度
            self._driver.implicitly_wait(1)
    #        判断异常处理的次数
            if self._error_num>self._max_num:
                raise e
            self._error_num+=1
            for ele in self._back_list:
                logging.info(ele)
                elelist=self._driver.find_elements(*ele)
                if len(elelist)>0:
                    elelist[0].click()
    #               处理完毕弹框，再去查找目标元素
                    return self.find(locator,value)
            # 这句代码是所有的黑名单都没有找到就会执行如下这句
            raise e


    def finds(self,locator,value:str=None,index:int=0):
        '''
        查询多个元素
        :param locator:
        :param value:
        :param index: 暂未使用此参数
        :return:
        '''
        logging.info(locator)
        logging.info(value)
        try:

            if isinstance(locator,tuple):
                elements=self._driver.find_elements(*locator)
            else:
                elements=self._driver.find_elements(locator,value)
            self._error_num=0
            self._driver.implicitly_wait(10)
            return elements
        except Exception as e:
            # 异常情况，需要调整等待时间，优化处理弹框的速度
            self._driver.implicitly_wait(1)
    #        判断异常处理的次数
            if self._error_num>self._max_num:
                raise e
            self._error_num+=1
            for ele in self._back_list:
                logging.info(ele)
                elelist=self._driver.find_elements(*ele)
                if len(elelist)>0:
                    elelist[0].click()
    #               处理完毕弹框，再去查找目标元素
                    return self.finds(locator,value)
            # 这句代码是所有的黑名单都没有找到就会执行如下这句
            raise e

    def scroll_ele_and_click(self, text_content,click=True):
        '''
        滚动到某个元素，
        :param click: 默认点击元素
        :param text_content: 元素的文本内容
        :return:
        '''
        if click:
            self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,

                f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text_content}").instance(0));'
            ).click()
        else:
            return self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,

                                      f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text_content}").instance(0));'
                                      )
    def find_and_get_text(self, locator, value: str = None):
        '''
        获取文本
        :param locator:
        :param value:
        :return:
        '''
        try:
            if isinstance(locator, tuple):
                element_text = self._driver.find_element(*locator).text
            else:
                element_text = self._driver.find_element(locator, value).text
            return element_text
        except Exception as e:
            # 异常情况，需要调整等待时间，优化处理弹框的速度
            self._driver.implicitly_wait(1)
            #        判断异常处理的次数
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for ele in self._back_list:
                logging.info(ele)
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    #               处理完毕弹框，再去查找目标元素
                    return self.find_and_get_text(locator, value)
            # 这句代码什么时候会执行啦
            raise e




