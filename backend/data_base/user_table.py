from datetime import datetime

# 用于生成具有时间维护的 token
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired

from backend.backend_server import app, db


class User(db.Model):
    """
    用户表，需要有账号，密码，邮箱
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    # 创建日期

    def __repr__(self):
        return f'<User {self.username}>'

    def generate_token(self, expires_in=3 * 3600):
        """
        生成 Token
        :return:
        """
        # app.config["SECRETY_KEY"]： token 种子，用于生成 token ，其值可以是随机的
        # expires_in 代表超时时间
        serializer = TimedJSONWebSignatureSerializer(app.config["SECRETY_KEY"], expires_in=expires_in)
        token_id = self.username + self.password + str(datetime.now())
        # dumps 用于反序列化（把 Python 对象转换成字符串），生成 Token
        token = serializer.dumps({"id": self.id, "token_id": token_id}).decode()
        return token

    # 方便外界进行调用，同时此方法不会用到对象中的数据
    @classmethod
    def check_token(cls, token):
        """
        校验 Token
        :return: User or None
        """
        serializer = TimedJSONWebSignatureSerializer(app.config["SECRETY_KEY"])
        try:
            # loads 用于序列化，把 Token 转换成 Python 对象
            token_loads_result = serializer.loads(token)
        # 如果 Token 校验失败，会抛出 BadSignature
        # 如果 Token 超时，会抛出 SignatureExpired
        except (BadSignature, SignatureExpired):
            return None
        # User.query.get 表示利用 id 找到 User 表中的一个字段
        return User.query.get(token_loads_result["id"])


#
# class Task(db.Model):
#     task_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.name


if __name__ == "__main__":
    # 删库
    db.drop_all()
    # 在远程数据库中创建表
    db.create_all()
