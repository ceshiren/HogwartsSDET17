from selenium.webdriver.common.by import By


def handle_black(fun):
    def run(*args, **kwargs):
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        # 相当于 self
        instance = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception:
            # 取出所有的妖魔鬼怪，一一进行处理
            for ele_xpath in black_list:
                # 用火眼晶晶去看，妖魔鬼怪是否存在
                eles = instance.finds(By.XPATH, ele_xpath)
                # 妖魔鬼怪出现了，需要斩杀
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)

    return run