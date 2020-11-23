from functools import reduce
# reduce 求 加减乘除

# def foo(x, y):
#     return x + y  # 第一次 x =100 y =89 第二次 x=189 y=76 以此类推
#
#
# scroe = [100, 89, 76, 97]
# print(reduce(foo, scroe))  # 362

student = [{'name': 'jerry', 'age': 80},
           {'name': 'jerry', 'age': 80},
           {'name': 'jerry', 'age': 80},]
# 第一次 x=0 y=80 第二次 x=80 y=80
def bar(x,y):
    return x+y['age']
print(reduce(bar,student,0))  # 240
print(reduce(lambda x,y:x+y['age'],student,0)) # 240 简化写法
