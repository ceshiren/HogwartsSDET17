"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/7 4:12 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from app.apppo.page.base_page import BasePage


class EditContactPage(BasePage):

    def edit_contact(self, name, phonenum):
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

    def verify_ok(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
