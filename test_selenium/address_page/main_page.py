from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.address_page.address_page import AddressPage


class MainPage:
    def __init__(self):
        # 声明 chrome 的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def goto_address(self):
        # 点击通讯录
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        return AddressPage(self.driver)