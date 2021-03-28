from test_requests.wework.base import Base


class WeworkAddress(Base):
    def get_information(self, user_id: str):
        """
        获取用户信息
        :param user_id:
        :return:
        """
        params = {"userid": user_id}
        r = self.send("GET", f"https://qyapi.weixin.qq.com/cgi-bin/user/get", params=params)
        return r.json()

    def create_member(self, user_id: str, name: str, mobile: str, department: list):
        """
        创建成员
        :param name:
        :param mobile: 手机号 11位
        :param department: 部门
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": department}
        r = self.send("POST", url, json=data)
        return r.json()

    def update(self, user_id, name: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": user_id,
            "name": name
        }
        r = self.send("POST", url, json=data)
        return r.json()

    def delete(self, user_id):
        params = {"userid": user_id}
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        r = self.send("GET", url, params=params)
        return r.json()
