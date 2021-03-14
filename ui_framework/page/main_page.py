from ui_framework.page.basepage import BasePage
from ui_framework.page.market import Market


class MainPage(BasePage):
    def goto_market(self):
        # self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        # self.find_and_click(By.XPATH ,'//*[@text="行情"]')
        self.parse("../page/main_page.yaml", "goto_market")

        return Market(self.driver)
