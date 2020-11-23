# filter 对可迭代对象进行过滤，得到的是一个filter对象
# 参数：第一个是函数  第二个是可迭代对象

age = [12, 23, 30, 17, 16, 22, 19]
x = filter(lambda ele: ele > 18, age)
# ptint(i)    # 结果：<filter object at 0x0000020333A669A0> 这是一个可迭代对象
adult = list(x)
print(adult)  # [23, 30, 22, 19]
