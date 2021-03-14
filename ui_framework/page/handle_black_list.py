import allure
from selenium.webdriver.common.by import By

from ui_framework.page.logger import log


def handle_black(fun):
    def run(*args, **kwargs):
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        # 相当于 self
        instance = args[0]
        try:
            log.debug("find " + args[2])
            return fun(*args, **kwargs)
        except Exception:
            # instance.screenshot()
            # with open("./tmp.png", "rb") as f:
            #     allure.attach(f.read(), attachment_type=allure.attachment_type.PNG)
            allure.attach(instance.screenshot(), attachment_type=allure.attachment_type.PNG)
            # 取出所有的妖魔鬼怪，一一进行处理
            for ele_xpath in black_list:
                # 用火眼晶晶去看，妖魔鬼怪是否存在
                eles = instance.finds(By.XPATH, ele_xpath)
                # 妖魔鬼怪出现了，需要斩杀
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)

    return run