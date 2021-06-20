from flask import request
from flask_restful import Resource

from backend.backend_server import db
from backend.data_base.user_table import User


class SignUp(Resource):
    """
    用户注册接口
    """
    def post(self):
        json = request.json
        new_user = User(**json)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        return {"msg": "OK", "errcode": 200}
