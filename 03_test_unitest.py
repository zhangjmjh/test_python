from selenium import webdriver
import unittest, time

# 四大组件
# test fixture  setUp  tearDown
# test case 测试用例 通过集成unitest TestCase 来实现用例的继承 在UniTest中，测试用例都是通过test来识别的
# test suite 测试套件 测试用例集
# test runner  运行器 一般通过runner来调用suit去执行测试
#unitest 运行机制 通过main函数中，调用unitest main()运行所有的内容

class BaiduTest(unittest.TestCase):  #通过继承unitest,TestCase来实现用例
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get('http://www.baidu.com')


    # 函数
    def plus(self, a ,b):
        c = a+b
        print(c)
        return c
    # 测试用例，加test才会认为你这个是测试用例
    def test_baidu(self):
        pass
    def test_youdao(self):
        pass
    def test_a(self):
        self.plus(1, 2)
        print('c')

    def tearDown(self):

if __name__ == '__main__':
    unittest.main()