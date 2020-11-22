# def add(a, b):
#     return a + b

# a = add(3, 4)
# fn = add  # 这里等于给函数 起一个 别名
# print(fn(1, 2))
# print(a)

# 除了使用def关键字定义一个函数以外，还可以使用lambda 表达式定义一个函数
# lambda a, b: a + b  # 匿名函数，用来表达一个简单的函数，函数调用的次数很少
# print(nul(1, 2))

def calc(a, b, fn):
    c = fn(a, b)
    return c


x1 = calc(5, 7, lambda x, y: x + y)
print(x1)  #12
