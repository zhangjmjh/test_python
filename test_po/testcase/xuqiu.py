
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from test_po.page.MainPage import MainPage
from time import sleep

class TestXueqiu(object):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://xueqiu.com/')
        main=MainPage(self.driver)

    # def test_search(self):
    #     pass
    #     #self.main.search("alibaba").follow("09988")
    #
    # def teardown(self):
    #     time.sleep(5)
    #     self.driver.quit()
