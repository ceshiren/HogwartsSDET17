"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/7 4:10 下午'
"""
# 添加成员页面
from appium.webdriver.common.mobileby import MobileBy

from app.apppo.page.base_page import BasePage
from app.apppo.page.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    def addcontact_menual(self):
        # 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditContactPage(self.driver)
