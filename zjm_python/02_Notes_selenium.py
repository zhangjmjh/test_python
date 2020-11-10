from selenium import webdriver    # 导入selenium的包
import unittest ,time   # 导入 unittest单元测试框架 和 时间的包

class Test_ret(unittest.TestCase):  # class 类（群） 后面加群名（Test_ret）第一个字母大写 括号里面规定写法

    def setUp(self):   # 测试用例的头部，也就是每次都要开始执行的操作，self默认参数，函数名默认
        self.driver = webdriver.Chrome()   # 指定使用Chrome浏览器
        self.driver.get("http://www.baidu.com")   # 需要打开的网站

    def tearDown(self):  # 测试用例的尾部，也就是每次都要开始执行的操作，self默认参数，函数名默认
        time.sleep(5)
        self.driver.quit()    # 关闭浏览器

    def test_wahaha(self):   # 正式的测试用例 def  + 开头 test作为文件名 + 想定义的名字

        self.driver.find_element_by_id("kw").send_keys("娃哈哈")   #  搜索哇哈哈
        time.sleep(5) # 挺顿5秒
        self.driver.find_element_by_id("su").click()    # 点击百度一下

    def test_sww(self):

        self.driver.find_element_by_id("kw").send_keys("爽歪歪")
        time.sleep(5) # 挺顿5秒
        self.driver.find_element_by_id("su").click()

    def test_ad(self):

        self.driver.find_element_by_id("kw").send_keys("AD钙奶")
        time.sleep(5) # 挺顿5秒
        self.driver.find_element_by_id("su").click()



if __name__ == '__main__':   # main 函数   和    class 一起搭配使用
    unittest.main()




# browser = webdriver.Chrome()   # 指定使用Chrome浏览器
#
# browser.get("http://www.baidu.com")   # 需要打开的网站
#
# browser.find_element_by_id("kw").send_keys("哈哈")  #  定位到输入框，输入搜索词 “哈哈”
#
# time.sleep(5) # 挺顿5秒
#
# browser.find_element_by_id("su").click()   #  定位到百度，点击操作
#
# time.sleep(5)
#
# browser.quit()    # 关闭浏览器



