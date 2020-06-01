# abby
import inspect
import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from appium_xueqiu_normal.page.wrapper import handle_back


class BasePage():
    _params={}
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_back
    def find(self, locator, value: str = None):
        '''
        查找元素
        :param locator: 定位方式 |定位方式和表达式
        :param value: 定位表达式
        :return:
        '''

        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def screenshot(self, name):
        '''
        截图
        :param name:图片名称
        :return:
        '''
        self._driver.save_screenshot(name)

    @handle_back
    def finds(self, locator, value: str = None, index: int = 0):
        '''
        查询多个元素
        :param locator:
        :param value:
        :param index: 暂未使用此参数
        :return:
        '''

        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_back
    def scroll_ele_and_click(self, text_content, click=True):
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

    @handle_back
    def find_and_get_text(self, locator, value: str = None):
        '''
        获取文本
        :param locator:
        :param value:
        :return:
        '''

        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    def steps(self, path):
        with open(path, encoding='utf-8')as f:
            # 方法名称
            # todo,不明白
            name = inspect.stack()[1].function
            # 取出字典中的一个元素，一个元素也就是对于page中的一个方法
            steps=yaml.safe_load(f)[name]
        #     序列化为字符串，为了替换变量
        raw=json.dumps(steps)
        for key,value in self._params.items():
            raw=raw.replace("${"+key+"}",value)
        # 反序列
        steps=json.loads(raw)
        # 取出方法中的步骤
        for step in steps:
            if "action" in step.keys():
                action=step['action']
                if "click"==action:
                    self.find(step['by'],step['locator']).click()
                # 执行send操作
                if 'send'==action:
                    self.find(step['by'],step['locator']).send_keys(step['value'])
                # 执行finds ,长度大于0 返回true
                if "len > 0"==action:
                    eles=self.finds(step['by'],step['locator'])
                    # 返回true  或false
                    return len(eles)>0
#
