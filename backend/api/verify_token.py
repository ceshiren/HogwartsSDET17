from flask import g
from flask_httpauth import HTTPBasicAuth



auth = HTTPBasicAuth()


"""
auth 的 username 在登陆时，是用户名。但是在登陆后，是 token
"""
# 编写回调函数，当进行登陆时，会回调此函数
@auth.verify_password
def verify_password(username, password):
    print(username)
    print(password)
    # 初始化 auth
    from backend.data_base.user_table import User
    # 进行 token 校验
    user = User.check_token(username)
    # 如果校验结果错误，或者超时。就认为此时是登陆接口
    # 如果校验成功，就认为此时是其它接口（获取用例）
    if not user:
        # 从数据库中查用户信息
        user = User.query.filter_by(username = username).first()
        # 如果用户不存在，或者密码不匹配，就检验失败
        if not user or user.password != password:
            return False
    # 如果 token 符合要求，或者用户名，密码正确
    # flask 的 g 代表 falsk 的本地线程变量 -> flask 线程可共享使用
    g.user = user
    return True
