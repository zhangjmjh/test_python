import datetime
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  #  以两个下划线开始的变量是私有属性

    def get_money(self):
        print('{}查询了余额'.format(datetime.datetime.now()))  # 2020-11-28 19:01:57.622389查询了余额
        return self.__money # 这里是可以访问到私有属性的



p = Person('张三',18)
# print(p.name, p.age)  # 张三 18
# print(p.__money)  # 不能够直接获取到私有变量

# 获取到私有变量的方式
# print(p._Person__money) # 1000

# print(p.get_money())  # 1000


# 修改私有变量的方法   定义一个函数
p.set_money(100)  #  不知道这里为啥打印不出来
print(p.set_money(100))


