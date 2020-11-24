import random

# 打印 randint(a,b) 用来生成 a-b之间的随机数
print(random.randint(2, 9))  # 7

# random()  随机生成0-1的随机浮点数
print(random.random())  # 0.6872035695381116

# randrange(a,b) 用来生成a-b的随机浮点数
print(random.randrange(2, 9))  # 6

# choice 用来在可迭代对象里随机抽取一个数据
print(random.choice(['zhangsan','lisi','jack']))  # jack

# sample 用来在可迭代对象里随机抽取两个数据
print(random.sample(['zhangsan','lisi','jack'],2))  # ['jack', 'zhangsan']