import requests


class TestAddress:
    def setup(self):
        self.token = self.get_token()

    def get_token(self):
        proxies = {"https": "http://127.0.0.1:8888"}
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe653983e4c732493&corpsecret=T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
        r = requests.get(url, proxies=proxies, verify=False)
        return r.json()['access_token']

    def test_get_information(self):
        user_id = 'm78001'
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}")
        print(r.json())

    def test_create_member(self):
        proxies = {"https": "http://127.0.0.1:8888"}
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "m78001",
            "name": "奥特曼",
            "mobile": "+86 13800004444",
            "department": [1]}
        r = requests.post(url, json=data, proxies=proxies, verify=False)
        print(r.json())

    def test_update(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": "m78001",
            "name": "迪迦"
        }
        r = requests.post(url, json=data)
        print(r.json())

    def test_delete(self):
        user_id = "m78001"
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}'
        r = requests.get(url)
        print(r.json())


