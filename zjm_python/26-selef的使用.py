class Student(object):
    # 下面这个属性是老大，是一个元组，用来规定对象可以存在的属性
    # 只有写了name 和 age  下面的函数才可以用这2个属性 否则不行
    __slots__ = ('name', 'age')

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好，我是', self.name)


# 1、调用了__new__方法，用来申请内存空间  0x00000292325B5430
# 2、调用了__init__方法传如参数，将self也指向创建好的内存空间
# 3、变量名也只指向了创建好的内存空间

s1 = Student('张三', 18)
s1.say_hello()  # 大家好，我是 张三

s2 = Student('jack', 21)
s2.say_hello()  # 大家好，我是 jack
