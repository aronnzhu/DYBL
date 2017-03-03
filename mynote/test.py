def deco(func):
    def _deco(*args, **kwargs):
        print("before myfunc() called.")
        func(*args)
        print("  after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco()

@deco
def myfunc(str a):
    print(" myfunc() called.")
    return 'ok'

myfunc('abc')
