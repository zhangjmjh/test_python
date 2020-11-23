# 多个未知数量的参数求和
def add_many(ret):
    x = 0
    for i in ret:
        x += i
    return x
a = add_many([1, 2, 3, 4, 5])
print(a) # 15


# *args  表示可变参数当传入的参数个数未知，且不需要知道参数名称时
def func_arg(farg, *args):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)
func_arg(1,"youzan",'dba','四块五的妞')
# formal arg: 1
# another arg: youzan
# another arg: dba
# another arg: 四块五的妞


# **kwargs:表示可变的关键字参数 可以接收任意数量关键词参数的
def add(a, b, *args,**kwargs):
    print('kwargs={}'.format(kwargs)) # kwargs={'k': 7, 'p': 9}
    c = a + b
    for i in args:
        c += i
    return c
ret = add(1, 3, 4,k=7,p=9)
print(ret) # 8


# **kwargs:
def fun(a, **kwargs):
    print("a is", a)  # a is 1
    print("b is", kwargs['b'])  # b is 3
    print("c is", kwargs['c'])#  c is 5
fun(1, b=3, c=5)