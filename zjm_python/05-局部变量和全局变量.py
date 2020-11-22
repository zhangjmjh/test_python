# 全局变量和局部变量
# a = 500
# def test():
#     x ="hello"
#     print('x={}'.format((x)))
#     a=10
#     print("函数内部的{}".format(a))
# test()
# print("函数外部的{}".format(a))

# global 修改全局变量 globals()查看全局变量 locals() 可以查看局部变量
# a = 500
# def test():
#     x = "hello"
#     print('x={}'.format((x)))
#     global a
#     a = 10
#     print("globals={},locals={}".format(globals(), locals()))
#     print("函数内部的{}".format(a))
# test()
# print("函数外部的{}".format(a))

# return 在函数中只能返回一次
def test(a, b):
    x = a // b
    y = a % b
    return x,y  #返回的本质是一个元组
result=test(13,5)
print("商是{}，余是{}".format(result[0],result[1]))
