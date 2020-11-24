class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):  # 对象被调用的时候使用
        pass

    def __repr__(self):
        return 'hello'

p = Person('zhangsan', 18)

print(p) # <__main__.Person object at 0x000001C6646E5430>

# 调用内置函数repr 会触发对象的 __repr__ 方法
print(repr(p))  #  hello