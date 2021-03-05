"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/4 9:02 下午'
"""
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# pip install appium-python-client
from appium import webdriver


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/igk")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gy9")
        el2.send_keys("霍格沃兹")
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView")
        el3.click()
