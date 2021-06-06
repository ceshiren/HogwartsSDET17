from datetime import datetime

from flask import Flask, request, g
# 初始化 Flask 实例
# Flask 是一个 wsgi 应用，（WSGI 是一套协议，使 Web 应用和服务器交互跟通顺）
# __name__ 给 Flask 一个名称
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

from backend.demo2 import User

app = Flask(__name__)
auth = HTTPBasicAuth()
CORS(app)


# 定义了路由，当访问路由中定义的 url 时，就会执行下面的函数
# / 代表根，也就是说，当浏览器什么都不输入的时候，就访问了根
@app.route("/")
def hello_world():
    # Flask 函数的返回值，默认是 html 类型
    # 如果返回是字典，就是 json 类型
    return "<p>Hello, World!</p>"


# methods 可以指定监听的类型，可以是　post get put ...
@app.route("/hello", methods=['POST'])
def hello():
    return "<p>Fine thank you!</p>"


# 可以通过 http://127.0.0.1:5000/param?a=b&c=k 来发送两个参数 a=b 和 c=k
@app.route("/param", methods=["POST"])
def get_param():
    # 可以利用 request.args 获取两个参数
    # 为什么 request.args 可以获取两个参数？ Thread-Local
    # 可以利用 request.json 获取 post 传过来的请求体
    return request.json


# Flask 中 <abc> 代表变量，会把真实 url 的 <abc> 中的内容传递给对应变量
@app.route("/param/<abc>")
def get_var(abc):
    return abc


# ----------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cekai_17:ceshiren.com@182.92.129.158:3306/test_backend_17'
# 初始化一个 db
db = SQLAlchemy(app)


# 验证token
@auth.verify_password
def verify_password(username_or_token, password):
    print(username_or_token)
    print(password)
    user = User.verify_auth_token(username_or_token)
    # 如果token不存在，验证用户id与密码是否匹配
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or user.password != password:
            return False
    g.user = user
    return True


@app.route("/login")
@auth.login_required
def login():
    token = g.user.generate_auth_token()
    return {"access_token": token.decode()}


@app.route("/get_info")
@auth.login_required
def get_information():
    return {"data": [{"id": 1234, "name": "hello"}, {"id": 345, "name": "hello2"}]}


@app.route("/register", methods=["POST"])
def register():
    user = User(**request.json, time=datetime.now())
    db.session.add(user)
    db.session.commit()
    print(request.json)

    return "OK"


# ---------------


if __name__ == '__main__':
    # 运行服务， Flask 默认会监听 127.0.0.1:5000 ，只要发送 get （或者其它）请求，就能触发路由
    # debug 参数：启动调式模式（当代码发生变化， Flask 会自动刷新，使改动生效）
    app.run(debug=True)
