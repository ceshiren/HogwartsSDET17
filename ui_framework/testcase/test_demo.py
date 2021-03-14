def b(fun):
    def run(*args, **kwargs):
        print("你好")
        fun(*args, **kwargs)
        print("再见")

    return run


@b
def a(k):
    print("我是 a ")
    print(k)

@b
def c():
    print("我是 c")

@b
def d():
    print("我是 d")


def test():
    # a("我是 k ")
    d()