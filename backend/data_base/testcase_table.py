from backend.backend_server import db


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)

    def as_dict(self):
        """
        返回测试用例的数据
        :return:
        """
        return {"id": self.id, "nodeid": self.nodeid, "description": self.description}
