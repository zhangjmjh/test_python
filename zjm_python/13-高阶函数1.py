# 1、一个函数作为另一个函数的参数
# 2、一个函数作为另一个函数的返回值
# 3、函数内部再定义一个函数

# def foo():
#     print('我是foo')
#     return 'foo'
#
# def bar():
#     print('我是bar')
#     return foo()
#
# x =bar()
# print('x的值是{}'.format((x)))
# 结果
# 我是bar
# 我是foo
# x的值是foo

# 函数调用函数
def outer():
    m=100
    def inner():
        n=90
        print('我是inner函数')
    print('我是outer函数')
    return inner()  # 又返回来调用inner 函数
outer() # 这里调用函数