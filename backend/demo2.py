from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature

app = Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cekai_17:ceshiren.com@182.92.129.158:3306/test_backend_17'
# 初始化一个 db
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "TMP123"

class User(db.Model):
    # 以下字段代表数据库中的表头
    # db.Integer 是整型，primary_key 代表主键，唯一标识一条数据，是一条数据的身份证
    id = db.Column(db.Integer, primary_key=True)
    # db.String（80） 代表 80 个字符的字符串
    # unique 代表是不是唯一
    # nullable 是否可为空，如果为 False ，说明为必填项
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    time = db.Column(db.Time(), unique=False, nullable=False)

    def generate_auth_token(self, expiration=600000):
        s = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        return User.query.get(data['id'])


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


if __name__ == "__main__":
    # 删库
    # db.drop_all()
    # 在远程数据库中创建表
    # db.create_all()

    # -----------------------------------添加
    # 向数据库中添加一条数据
    # 实例化 User 类
    # for i in range(1, 20):
    #     data = User(username="wangwu" + str(i), description="i'm wangwu")
    #     # 把类添加到 sqlalchemy 中
    #     db.session.add(data)
    # # 把操作提交
    # db.session.commit()
    #
    # # -----------------------------------查询
    # # 查询
    # # 在 User 表中查数据，就使用 User.query
    # 可以使用 query.filter_by(name='123').all() 指：返回所有结果 ， first 获取第一个结果
    # 可以使用 query.all() 找出所有数据，再利用 python 语法进行过滤
    # result = User.query.all()
    # result = [i for i in result if "0" in i.username]

    # -----------------------------------更新
    #  先过滤出想要修改的数据，然后对数据进行修改，修改完成后可以使用 db.session.commit() 进行提交
    # user = User.query.filter_by(username='wangwu1').first()
    # print(type(user))
    # user.description = "hello"
    # db.session.commit()
    # -----------------------------------删除
    # 先过滤出想删除的数据，然后利用 db.session.delete(user) 进行删除，最终需要 db.session.commit() 进行提交
    user = User.query.filter_by(username='wangwu1').first()
    db.session.delete(user)
    db.session.commit()
