from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.XPATH, "//*[@id='corp_name']").send_keys("xxxxx")
