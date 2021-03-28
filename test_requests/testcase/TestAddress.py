from test_requests.wework.WeworkAddress import WeworkAddress


class TestAddress:
    def setup_class(self):
        self.address = WeworkAddress()

    def setup(self):
        # 数据库
        self.address.delete()

    def teardown(self):
        self.address.delete()

    def test_get_information(self):
        # 数据处理
        self.address.create_member()

        # 用户信息是不是正确
        r = self.address.get_information()
        assert r["name"] == "奥特曼"

    def test_crate_member(self):
        r = self.address.create_member()
        assert r.get("errmsg") == "created"
        # 断言
        info = self.address.get_information()
        assert info['name'] == "奥特曼"

    def test_update_member(self):
        self.address.create_member()
        r = self.address.update()
        assert r.get("errmsg") == "updated"
        # 断言
        info = self.address.get_information()
        assert info['name'] == "迪迦"

    def test_delte_member(self):
        self.address.create_member()
        r = self.address.delete()
        assert r.get("errmsg") == "deleted"
        # 断言
        info = self.address.get_information()
        assert info['errcode'] == 60111
