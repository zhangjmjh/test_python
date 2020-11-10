
from selenium import webdriver

# 这个页面是selenium的一些基础操作，比如打开网页，隐式等待，这是一个基础的page，叫BasePage的类
#所以很多页面都需要引用这个页面

class BasePage:
    base_uarl = ""

    def __init__(self, driver = None):
        if driver != None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver

        self.driver.implicitly_wait(10)
        if self.base_uarl != "":
            self.driver.get(self.base_uarl)
            self.driver.find_element_by_class_name()
