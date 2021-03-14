import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from ui_framework.page.handle_black_list import handle_black
from ui_framework.page.logger import log


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def find_and_click(self, locator, value):
        self.find(locator, value).click()

    def find_and_send(self, locator, value, content):
        self.find(locator, value).send_keys(content)

    def screenshot(self):
        # self.driver.save_screenshot("tmp.png")
        return self.driver.get_screenshot_as_png()

    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次， 未找到。")
            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def parse(self, yaml_path, fun_name):
        """
        解析关键字，实现相应动作
        :param yaml_path:
        :param fun_name:
        :return:
        """
        with open(yaml_path, "r", encoding="utf-8") as f:
            function = yaml.load(f)
            # 从关键字中取出一个函数
        steps = function.get(fun_name)
        # 解析每一组关键字
        for step in steps:
            # 如果发现关键字是 find_and_click ，就调用已经封装好的 find_and_click 即可
            if step.get("action") == "find_and_click":
                self.find_and_click(step.get('locator'), step.get('value'))
            elif step.get("action") == "find_and_send":
                self.find_and_send(step.get('locator'), step.get('value'), step.get('content'))
