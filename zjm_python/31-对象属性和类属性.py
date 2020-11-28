class Person(object):
    type = '人类'
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 对象p1和p2都是通过Person 类创建出来的  称为实例对象
# name 和 age 是对象属性
# Person  称为类对象
# 只要创建了一个实例对象，这个实例对象就有自己的name和age属性 下面p1和p2 都有各自的name和age 属性

p1 = Person('张三',18)
p2 = Person('李四',10)


# 也可以通过实例对象来获取类属性
print(p1.type)
print(p2.type)


# 类属性只能通过类对象来修改，实例对象无法修改类属性
p1.type = 'human'
print(p1.type) # 并不会修改类属性，而是给实例对象添加一个新的对象属性
print(Person.type)   # 人类