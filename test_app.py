from appium import webdriver
import pytest
from zfx_app_element import is_element_present
import time


class TestSearch():
    def setup(self):     #  初始化整个APP运行环境
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '7XBRX18B15002828',
            'platformVersion': '10',
            'appPackage': 'com.shenzhen.yirabbit',
            'appActivity': 'com.shenzhen.yirabbit.ui.activity.WelComeActivity',
            'newCommandTimeout': 2000,
            'automationName': 'UiAutomator2',
            'noReset': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    # def test_login(self):  #  判断登陆是否成功
    #
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/loginButton").click()  # 登陆
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/account").clear()
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/account").send_keys('18800000000')
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/password").clear()
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/password").send_keys('Qo123456')
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/finishButton").click()  #登陆
    #     self.driver.implicitly_wait(15)
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  #   关闭活动弹窗
    #     is_element_present(self.driver, 'id', 'com.shenzhen.yirabbit:id/haveNotice')

    # def test_market_buy(self):
    #     """
    #     市价买入澳元兑日元后平仓
    #     :return:
    #     """
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()    #  交易
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  #  去下单
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()   # 外汇
    #     self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()   # 澳元兑日元
    #     self.driver.find_element_by_android_uiautomator('text(\"买入\")').click()   # 买入澳元兑日元
    #     self.driver.find_element_by_android_uiautomator('text(\"确认开仓\")').click()  # 确认开仓
    #     self.driver.find_element_by_id('com.shenzhen.yirabbit:id/viewPendingOrder').click()  #  查看持仓
    #     self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.ViewAnimator/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout").click()
    #     self.driver.find_element_by_android_uiautomator('text(\"平仓\")').click()
    #     self.driver.find_element_by_id('com.shenzhen.yirabbit:id/sureOpenButton').click()
    #     self.driver.find_element_by_android_uiautomator('text(\"查看持仓\")').click()  # 查看持仓

    # def test_market_sell(self):
    #     """
    #     市价卖出澳元兑日元后平仓
    #     :return:
    #     """
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
    #     self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  # 去下单
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()  # 外汇
    #     self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()  # 澳元兑日元
    #     self.driver.find_element_by_android_uiautomator('text(\"卖出\")').click()  # 卖出澳元兑日元
    #     self.driver.find_element_by_android_uiautomator('text(\"确认开仓\")').click()  # 确认开仓
    #     self.driver.find_element_by_id('com.shenzhen.yirabbit:id/viewPendingOrder').click()  # 查看持仓
    #     self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.ViewAnimator/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout").click()
    #     self.driver.find_element_by_android_uiautomator('text(\"平仓\")').click()      #  平仓
    #     self.driver.find_element_by_id('com.shenzhen.yirabbit:id/sureOpenButton').click()   #  平仓
    #     self.driver.find_element_by_android_uiautomator('text(\"查看持仓\")').click()  # 查看持仓

    def test_limit_buy(self):
        """
        限价买入澳元兑日元后撤单
        :return:
        """
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  # 去下单
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()  # 外汇
        self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()  # 澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"买入\")').click()  # 买入澳元兑日元
        #self.driver.find_element_by_id('com.shenzhen.yirabbit:id/iv_guadan_arrow').click()  #  挂单
        self.driver.find_element_by_android_uiautomator('text(\"挂单\")').click()  # 挂单
        self.driver.find_element_by_android_uiautomator('text(\"限价\")').click()  # 限价
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView[1]').click()
        self.driver.find_element_by_android_uiautomator('text(\"确认挂单\")').click()  # 确认挂单
        self.driver.find_element_by_android_uiautomator('text(\"查看挂单\")').click()  # 查看挂单
        self.driver.find_element_by_android_uiautomator('text(\"限价挂单\")').click()  # 限价挂单
        self.driver.find_element_by_android_uiautomator('text(\"撤单\")').click()  # 限价撤单
        self.driver.find_element_by_android_uiautomator('text(\"确认\")').click()  # 限价撤单

    def test_limit_sell(self):
        """
        限价卖出澳元兑日元后撤单
        :return:
        """
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  # 去下单
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()  # 外汇
        self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()  # 澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"卖出\")').click()  # 卖出澳元兑日元
        # self.driver.find_element_by_id('com.shenzhen.yirabbit:id/iv_guadan_arrow').click()  #  挂单
        self.driver.find_element_by_android_uiautomator('text(\"挂单\")').click()  # 挂单
        self.driver.find_element_by_android_uiautomator('text(\"限价\")').click()  # 限价
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView[2]').click()
        self.driver.find_element_by_android_uiautomator('text(\"确认挂单\")').click()  # 确认挂单
        self.driver.find_element_by_android_uiautomator('text(\"查看挂单\")').click()  # 查看挂单
        self.driver.find_element_by_android_uiautomator('text(\"限价挂单\")').click()  # 限价挂单
        self.driver.find_element_by_android_uiautomator('text(\"撤单\")').click()  # 限价撤单
        self.driver.find_element_by_android_uiautomator('text(\"确认\")').click()  # 限价撤单

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()

