import requests
def request_demo():
    res = requests.request(method="GET", url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww93348658d7c66ef4&corpsecret=T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw")


if __name__ == '__main__':
    request_demo()