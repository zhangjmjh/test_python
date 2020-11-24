class Student(object):
    def __init__(self, name, age, height):  # 关注这个类有哪些特征和行为
        # 在__init__方法里，以参数的形式定义特征，称之为属性
        self.name = name
        self.age = age
        self.height = height

    # 行为定义为一个个函数
    def run(self):
        print('正在跑步')

    def eat(self):
        print('正在吃东西')


# 使用Student 类创建了两个实例对象 s1 s2
# s1和s2 都会有name  age   height 属性 同时都有run 和 eat 方法
s1 = Student('小明', 18, 1.75)  # Student() 会自动调用 init 方法
s2 = Student('小花', 18, 1.75)