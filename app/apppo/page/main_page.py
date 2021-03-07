"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/7 4:05 下午'
"""
# 主页
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.apppo.page.addresslist_page import AddressListPage
from app.apppo.page.base_page import BasePage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addresslist(self):
        # 点击 通讯录
        self.find(*self.addresslist_element).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
