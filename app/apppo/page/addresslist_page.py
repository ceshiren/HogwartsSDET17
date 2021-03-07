"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/7 4:08 下午'
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from app.apppo.page.addcontact_page import AddContactPage
from app.apppo.page.base_page import BasePage


class AddressListPage(BasePage):

    def click_addcontact(self):
        element = self.swipe_find("添加成员")
        element.click()
        return AddContactPage(self.driver)
