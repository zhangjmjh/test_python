from appium import webdriver
import pytest
# import unittest
from zfx_app_element import is_element_present
# from appium.common.exceptions import NoSuchElementException
# import time


class TestSearch():
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '7XBRX18B15002828',
            'platformVersion': '10',
            'appPackage': 'com.shenzhen.yirabbit',
            'appActivity': 'com.shenzhen.yirabbit.ui.activity.WelComeActivity',
            'newCommandTimeout': 2000,
            'automationName': 'UiAutomator2'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_always_button').click()
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.shenzhen.yirabbit:id/confirm').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.shenzhen.yirabbit:id/closeImage').click()
        self.driver.implicitly_wait(10)

    def test_login(self):  #  登陆
        self.driver.find_element_by_id('com.shenzhen.yirabbit:id/priceRadioButton').click()   # 协议
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/loginButton").click()  # 弹窗
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/account").send_keys('18800000000')
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/password").send_keys('Qo123456')
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/finishButton").click()  #登陆
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  #   关闭活动弹窗
        #self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()    #  交易
        #self.driver.find_element_by_id('com.shenzhen.yirabbit:id/sureOpenButton').click()  #  新手指引(知道了)
        # self.driver.find_element_by_id('com.shenzhen.yirabbit:id/sureOpenButton')  #  断言出现新手指引登陆成功
        is_element_present(self.driver, 'id', 'com.shenzhen.yirabbit:id/haveNotic')

    # def test_transaction(self):  # 投票
    #     pass

    def teardown(self):
        # time.sleep(5)
        # self.driver.quit()
        pass

if __name__ == '__main__':
    pytest.main()


