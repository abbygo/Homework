# abby
import logging
import os

import allure
from selenium.webdriver.common.by import By
from appium_xueqiu_normal.common.dir_config import screenshot_root_dir

def handle_back(func):
    '''
    处理黑名单
    :param func: 方法名
    :return:
    '''
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        '''
        异常处理
        :param args: 传入方法的参数
        :param kwargs: 传入方法的参数
        :return:
        '''
        # logging.info('run method：{0}\n;args{1}\n;kargs{2}').format(func.__name__, str(args[1:]), str(kwargs))
        # str(kwargs) ,转换为str ,其中内容必须不能为空，否则会报错；空对象不能格式化   AttributeError: 'NoneType' object has no attribute 'format'
        logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
        # 黑名单列表
        _back_list = [
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),

        ]
        from appium_xueqiu_normal.page.base_page import BasePage
        # 这里需要局部导入，避免循环导入；其中args[0] 就是basepage
        instance: BasePage = args[0]
        # 错误次数
        _error_num = 0
        # 最大错误次数
        _max_num = 3
        try:
            element = func(*args, **kwargs)
            _error_num = 0
            instance._driver.implicitly_wait(10)
            # 这里记得返回数据
            return element
        except Exception as e:
            file_name=os.path.join(screenshot_root_dir,'tmp.png')
            instance.screenshot(file_name)
            # 这里的文件名
            with open(file_name,'rb') as file:
                content=file.read()
            #     把图片加载到allure
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            logging.error("element not found, handle black list")
            # 异常情况，需要调整等待时间，优化处理弹框的速度
            instance._driver.implicitly_wait(1)
            #        判断异常处理的次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _back_list:
                logging.info(ele)
                elelist = instance._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    #               处理完毕弹框，再去查找目标元素
                    return func(*args, **kwargs)
            # 这句代码是所有的黑名单都没有找到元素就会执行如下这句
            raise e

    return wrapper
