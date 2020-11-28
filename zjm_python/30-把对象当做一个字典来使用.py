class Person(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __setitem__(self, key, value):
        p.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

p = Person('张三',18,'襄阳')
print(p.__dict__)  # 将对象转换成为字典  # {'name': '张三', 'age': 18, 'city': '襄阳'}
# 不能直接把一个对象当做字典来使用
p['age'] = 20  # []语法会调用对象的__setitem__方法
print(p.name)  # 张三

print(p.name,p.age)  # 会调用__getitem__方法
print(p['name'])