from flask import g
from flask_restful import Resource

from backend.api.verify_token import auth



class Login(Resource):
    # auth.login_required 是 httpAuth 的用法，添加了此装饰器的对象会回调校验方法
    # method_decorators 代表给 Login 接口添加一个装饰器，下面的 get 表示对 get 接口进行添加
    method_decorators = {'get': [auth.login_required]}

    def get(self):
        # 使用 verify_password 中，校验成功后的用户信息
        token = g.user.generate_token()
        return {"access_token": token}

