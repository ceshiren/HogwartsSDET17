class A:
    # 打印类 A 的信息
    def __repr__(self):
        return "hello"



def test_a():
    a = A()
    print(a)
