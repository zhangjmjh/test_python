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