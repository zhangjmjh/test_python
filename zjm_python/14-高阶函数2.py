# 1、一个函数作为另一个函数的参数
def ret():
    print('test函数')
    return 'hello'
def demo():
    print('demo函数')
    return ret
def bar():
    print('bar函数')
    return ret()

# a = bar()
# print(a) # bar函数 test函数  hello

# x = ret()
# print(x)  # test函数  hello

y = demo()
print(y)  # demo函数  y 等于 ret函数
z = y()
print(z)  #  test函数  z=hello
