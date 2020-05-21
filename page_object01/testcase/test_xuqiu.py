
import unittest

class TestXueqiu(object):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get('https://xueqiu.com/')


    def test_search(self):



    def teardown(self):
        time.sleep(5)
        self.driver.quit()
