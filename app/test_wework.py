"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/4 9:02 下午'
"""
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# pip install appium-python-client
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        '''
        前提条件: 已登录状态（ noReset=True）
        打卡用例：
        1、打开【企业微信】应用
        2、进入【工作台】
        3、点击【打卡】
        4、选择【外出打卡】tab
        5、点击【第N次打卡】
        6、验证【外出打卡成功】
        7、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='工作台']").click()
        # android_uiautomator 里面要用双引号，外面用单引号。
        # 向下滑动两次，再向上查找，直到找到元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        print(self.driver.page_source)
        # sleep(2)
        # assert "外出打卡成功" in self.driver.page_source
        # 激活隐式等待
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
