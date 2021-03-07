"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/7 2:42 下午'
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from time import sleep

from selenium.common.exceptions import NoSuchElementException


class TestContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # 跳过安装uiautomator2server等 服务
        caps['skipServerInstallation'] = "true"
        # 跳过设备的初始化
        caps['skipDeviceInitialization'] = "true"
        # 运行前不停止app
        # caps['dontStopAppOnReset'] = "true"

        # caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

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

    def test_addcontact(self):
        name = "hogwarts_2"
        phonenum = "13100000002"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        element = self.swipe_find("添加成员")
        element.click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 验证添加成员 toast
        # sleep(1)
        # print(self.driver.page_source)
        # assert '添加成功' in self.driver.page_source
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")

    def test_delcontact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/igk").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys("hogwarts_011")
        elelist = self.driver.find_elements(MobileBy.XPATH, "//*[@text='hogwarts_011']")
        # find_elements 方法返回的是一个列表 [element1, element2.....]
        if len(elelist) > 1:
            elelist[1].click()
