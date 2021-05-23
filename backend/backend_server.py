from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cekai_17:ceshiren.com@182.92.129.158:3306/test_backend_17'
# 初始化一个 db
db = SQLAlchemy(app)
# 将 flask 实例加载到 flask-restful 中
api = Api(app)


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


# 定义测试用例接口
class TestCaseAdd(Resource):
    def post(self):
        """
        新增用例
        :return:
        """
        # 把请求体中的数据，发送到数据库
        data = TestCase(**request.json)
        db.session.add(data)
        db.session.commit()
        return {"msg": "OK"}


class TestCaseDelete(Resource):
    # get 方法代表接收 get 请求
    def get(self):
        """
        删除测试用例
        :return:
        """
        # 如果 url 中存在 option 参数为 del_testcase 代表要删除用例
        if "nodeid" in request.args:
            # 利用 nodeid 参数指明要删除的用例
            nodeid = request.args.get("nodeid")
            # 查询此用例后，进行删除
            testcase = TestCase.query.filter_by(nodeid=nodeid).first()
            db.session.delete(testcase)
            db.session.commit()
            return {"msg": "delete success"}
        # 删除多个用例，比如 '[nodeid_1, nodeid_2, nodeid_3]'
        elif "nodeids" in request.args:
            # 利用 nodeid 参数指明要删除的用例
            nodeids = request.args.get("nodeids")
            for nodeid in nodeids.split(","):
                # 查询此用例后，进行删除
                testcase = TestCase.query.filter_by(nodeid=nodeid).first()
                db.session.delete(testcase)
            db.session.commit()
            return {"msg": "delete success"}


class TestCaseUpdate(Resource):
    """
    更新测试用例
    """

    def post(self):
        request_body = request.json
        # 查询出要更新的数据
        testcase = TestCase.query.filter_by(nodeid=request_body.get("nodeid")).first()
        # 更新数据的描述信息
        testcase.description = request_body.get("description")
        db.session.commit()
        return {"msg": "update success"}

class TestCaseGet(Resource):
    def get(self):
        # 查找所有测试用例
        test_cases = TestCase.query.all()
        # 对测试用例进行格式化
        format_test_cases = [i.as_dict() for i in test_cases]
        return format_test_cases


# 增加路由
api.add_resource(TestCaseAdd, '/testcase/add')
api.add_resource(TestCaseDelete, '/testcase/delete')
api.add_resource(TestCaseGet, '/testcase/get')
api.add_resource(TestCaseUpdate, '/testcase/update')

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # for i in range(5):
    #     data = TestCase(nodeid='nodeid_' + str(i))
    #     db.session.add(data)
    # db.session.commit()
    app.run(debug=True)
