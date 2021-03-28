import requests


class WeworkAddress:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": "wwe653983e4c732493",
                  "corpsecret": "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"}
        r = requests.get(url, params=params)
        return r.json()['access_token']

    def get_information(self, user_id: str):
        """
        获取用户信息
        :param user_id:
        :return:
        """
        params = {"access_token": self.token,
                  "userid": user_id}
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get", params=params)
        return r.json()

    def create_member(self, name: str, mobile: str, department: list):
        """
        创建成员
        :param name:
        :param mobile: 手机号 11位
        :param department: 部门
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "m78001",
            "name": name,
            "mobile": mobile,
            "department": department}
        r = requests.post(url, json=data)
        return r.json()

    def update(self, user_id, name: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": user_id,
            "name": name
        }
        r = requests.post(url, json=data)
        return r.json()

    def delete(self, user_id):
        params = {"access_token": self.token,
                  "userid": user_id}
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        r = requests.get(url, params=params)
        return r.json()
