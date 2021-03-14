from ui_framework.page.basepage import BasePage


class Search(BasePage):
    def search(self):
        # self.find_and_send(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
        self.parse("../page/search.yaml", "search")
