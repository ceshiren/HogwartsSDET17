import requests
def request_demo():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    param = {
        "corpid":"ww93348658d7c66ef4",
        "corpsecret":"T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"
    }
    proxy = {
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080"
    }
    res = requests.get(url=url, params=param, proxies =proxy, verify = False)



if __name__ == '__main__':
    request_demo()