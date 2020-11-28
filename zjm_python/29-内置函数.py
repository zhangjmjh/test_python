class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name + '正在吃饭')

p = Person('张三',18)
print((p.__dict__))  # {'name': '张三', 'age': 18}