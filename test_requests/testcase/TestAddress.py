import pytest

from test_requests.wework.WeworkAddress import WeworkAddress


class TestAddress:
    name = "kenan_"
    user_id = "kenan001"

    def setup_class(self):
        self.address = WeworkAddress()

        self.mobile = "13790776890"
        self.department = [1]

    def setup(self):
        # 数据库
        self.user_id += "tmp"
        self.address.delete(self.user_id)

    def teardown(self):
        self.address.delete(self.user_id)

    def test_get_information(self):
        # 数据处理
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)

        # 用户信息是不是正确
        r = self.address.get_information(self.user_id)
        assert r["name"] == self.name

    def test_crate_member(self):
        r = self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        assert r.get("errmsg") == "created"
        # 断言
        info = self.address.get_information(self.user_id)
        assert info['name'] == self.name

    @pytest.mark.parametrize("user_id, new_name", [("tmp", name + "tmp")]*30)
    def test_update_member(self, user_id, new_name):
        user_id += self.user_id
        self.address.create_member(user_id, self.name, self.mobile, self.department)
        r = self.address.update(user_id, new_name)
        assert r.get("errmsg") == "updated"
        # 断言
        info = self.address.get_information(user_id)
        assert info['name'] == new_name

    def test_delte_member(self):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.delete(self.user_id)
        assert r.get("errmsg") == "deleted"
        # 断言
        info = self.address.get_information(self.user_id)
        assert info['errcode'] == 60111
