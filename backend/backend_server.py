from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cekai_17:ceshiren.com@182.92.129.158:3306/test_backend_17'
# 将 flask 实例加载到 flask-restful 中
app.config["SECRETY_KEY"] = "SDET17"
api = Api(app)
db = SQLAlchemy(app)
# 使用 CORS 解决同源问题
CORS(app)


def router():
    from backend.api.testcase import TestCaseAdd
    api.add_resource(TestCaseAdd, '/testcase/add')
    from backend.api.testcase import TestCaseDelete
    api.add_resource(TestCaseDelete, '/testcase/delete')
    from backend.api.testcase import TestCaseGet
    api.add_resource(TestCaseGet, '/testcase/get')
    from backend.api.testcase import TestCaseUpdate
    api.add_resource(TestCaseUpdate, '/testcase/update')
    from backend.api.testcase import TestCaseRun
    api.add_resource(TestCaseRun, '/testcase/run')
    from backend.api.login import Login
    api.add_resource(Login, '/login')
    from backend.api.signup import SignUp
    api.add_resource(SignUp, '/signup')


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # for i in range(5):
    #     data = TestCase(nodeid='nodeid_' + str(i))
    #     db.session.add(data)
    # db.session.commit()
    router()
    app.run(debug=True)
