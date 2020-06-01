#abby
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_normal.page.base_page import BasePage
from appium_xueqiu_normal.page.search import Search


class Market(BasePage):
    def goto_search(self):
        return Search(self._driver)