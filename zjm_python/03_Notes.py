"""
XPATH写法:
//android.view.ViewGroup   #  根据 class  属性
//*[@resource-id='com.shenzhen.yirabbit:id/labels']/android.widget.TextView[1]  # 根据resource-id 的上层节点来定位
"""

"""
pytest常用的插件:
pytest-allure    生成allure 报告
    pytest --alluredir=output   输出allure报告
    allure serve output    查看allure报告
pytest-sugar    优化运行效果
pytest-rerunfailures    重新运行错误用例
    pytest --reruns = 2 test_app.py    失败后重新运行2次  最后才标记失败
    pytest --reruns = 2 test_app.py --reruns-delay = 2   加延时
pytest-assume   断言 多条断言失败也都运行
pytest-html   测试报告
pytest fixture  一种常用或基本的操作可以提前先定义好，比如登陆和退出，
    @pytest.fixture()
    def login():
        print('这是一个登陆方法')
    def test_case001(login):     这里会先去调用登陆方法，再执行下面的用例
        print('这是测试用例1')
    def test_case002():
        print('这是测试用例2')
"""

'''
面向对象编程
类的三要素：
1、类名： 这类事物的名字，满足大驼峰命名方法（首字母大写，单词与单词之间不用下划线）
2、属性：这类事物具体有什么特征
3、方法：这类事物具有什样的行为
在初始化方法内部定义属性
class Cat:
    def __init__(self , new_name):  # 增加了一个形参，这是对象的某些默认属性，初始化的同时设置初始值
        print('这是一个初始化方法')
        # self. 属性名 = 属性的初始值,下面就是定义属性的方式
        #self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

创建猫对象，使用类名()创建对象的时候，会自动调用初始化方法  __init__
这种一个类名() 系统会在内部创建一个小格子，然后运行上面的初始化方法，初始化方法里面给self增加了一个name的属性
并把Tom指向了这个name属性，最后打印tom的属性时，就会出现name的属性
tom = Cat("小猫")
tom.eat()
lazy_cat = Cat("大猫")
lazy_cat.eat()

'''

"""
from selenium import webdriver
import unittest ,time
from ddt import ddt, data
# 四大组件
# test fixture  setUp  tearDown
# test case 测试用例 通过集成unitest TestCase 来实现用例的继承 在UniTest中，测试用例都是通过test来识别的
# test suite 测试套件 测试用例集
# test runner  运行器 一般通过runner来调用suit去执行测试
#unitest 运行机制 通过main函数中，调用unitest main()运行所有的内容

@ddt
class TestLogin(unittest.TestCase):  #通过继承unitest,TestCase来实现用例
    # 类的初始化    在所有的用例运行之前先初始化所有的类，或者是释放整个类中的资源
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("ret1")
    #
    # #  类的释放
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('ret2')

    #  这里是用例的初始化
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    # 测试用例，加test才会认为你这个是测试用例
    # ddt的基本使用，在class的类前定义@ddt，用于表示要使用ddt了，再基于实际的应用，在data中写入我要传入的测试数据
    # ddt其实就是一个装饰器


    @data(('网易'), ('腾讯'))
    def test_baidu(self ,txt):     #  这里我只传入了一个参数，所以这里就只能写一个参数11
        self.driver.find_element_by_id('kw').send_keys(txt)
        self.driver.find_element_by_id('su').click()


if __name__ == '__main__':
    unittest.main()

"""

import requests
import json


class RunMain:

    def send_get(self, url, data):
        r = requests.get(url=url, params=data).json()
        return r

    def send_post(self, url, data):
        r = requests.post(url=url, data=data).json()
        return r

    def run_main(self, url, methon, data=None):
        r = None
        if methon == 'GET':
            r = self.send_get(url, data)
        else:
            r = self.send_post(url, data)
        return r


if __name__ == '__main__':
    url = 'http://web.juhe.cn:8080/finance/stock/hs'
    data = {'key': '1c705503c9bc44c87227fdfb854557c6', 'gid': 'sh601009'}
    run = RunMain()
    print(run.run_main(url, 'GET', data))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('jack', 18)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


bart = Student('jack', 99)
print(bart.name)


class Student1(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%d' % (self.name, self.score))


bart = Student('jack', 99)
print(bart.score)

# #  调用函数
# from abstest import my_abs    # 这里我是在调用 abstest （文件名，不含.py的扩展名  导入 my_abs这个函数名来获取的）
# print(my_abs(-888))           # 注意一定要在同一个目录文件下，不在同一个目录文件下是调用不了的


#  位置参数

# def power(x ,n):     #  这里首先记住是必须传了2个参数，循环了2次，第一次是 n =2 循环了一次，s=5  n=1 继续循环了一次第二次
#     s = 1            #   n=1的时候还循环了一次
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5 ,2))
