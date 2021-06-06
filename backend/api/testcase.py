# 定义测试用例接口
from flask import request
from flask_restful import Resource

from backend.api.verify_token import auth
from backend.backend_server import db
from backend.data_base.testcase_table import TestCase


class TestCaseAdd(Resource):
    method_decorators = [auth.login_required]

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
    method_decorators = [auth.login_required]

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
    method_decorators = [auth.login_required]

    def post(self):
        request_body = request.json
        # 查询出要更新的数据
        testcase = TestCase.query.filter_by(nodeid=request_body.get("nodeid")).first()
        # 更新数据的描述信息
        testcase.description = request_body.get("description")
        db.session.commit()
        return {"msg": "update success"}


class TestCaseGet(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        # 查找所有测试用例
        test_cases = TestCase.query.all()
        # 对测试用例进行格式化
        format_test_cases = [i.as_dict() for i in test_cases]
        return {"msg":"OK", "data": format_test_cases}
