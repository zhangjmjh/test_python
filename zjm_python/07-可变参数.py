# 多个未知数量的参数求和
# def add_many(ret):
#     x = 0
#     for i in ret:
#         x += i
#     return x
# a = add_many([1, 2, 3, 4, 5])
# print(a)

# *args  表示可变参数  **kwargs表示可变的关键字参数
def add(a, b, *args,**kwargs):
    print('kwargs={}'.format(kwargs))
    c = a + b
    for i in args:
        c += i
    return c


ret = add(1, 3, 4,k=7,p=9)
print(ret)
