from appium import webdriver
import pytest
from zfx_app.zfx_app_element import is_element_present
import time
import allure
import os


@allure.feature('对整个APP进行登陆断言、市价买入卖出并分批次平仓、停损挂单买入卖出并分批次平仓、限价挂单买入卖出并分批次平仓')
class TestSearch():

    @allure.story('初始化整个APP运行环境')
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '7XBRX18B15002828',    #  华为手机
            'platformVersion': '10',
            'appPackage': 'com.shenzhen.yirabbit',
            'appActivity': 'com.shenzhen.yirabbit.ui.activity.WelComeActivity',
            'newCommandTimeout': 2000,
            'automationName': 'UiAutomator2',
            'noReset': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    @allure.story('判断登陆 是否成功')
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    def test_login(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/loginButton").click()  # 登陆
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/account").clear()
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/account").send_keys('17111114444')
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/password").clear()
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/password").send_keys('Qo123456')
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/finishButton").click()  #登陆
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  #   关闭活动弹窗
        self.driver.implicitly_wait(15)
        is_element_present(self.driver, 'id', 'com.shenzhen.yirabbit:id/haveNotice')  #  断言出现平台公告的角标认为登陆成功

    @allure.story('市价买入 澳元兑日元 平仓')
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    def test_market_buy(self):
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()    #  交易
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  #  去下单
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()   # 外汇
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()   # 澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"买入\")').click()   # 买入澳元兑日元
        self.driver.find_element_by_xpath("//*[@resource-id='com.shenzhen.yirabbit:id/labels']/android.widget.TextView[2]").click()  # 开仓0.2手
        self.driver.find_element_by_android_uiautomator('text(\"确认开仓\")').click()  # 确认开仓
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.shenzhen.yirabbit:id/viewPendingOrder').click()  #  查看持仓
        self.driver.implicitly_wait(10)

        # 第一次平仓0.05手
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/rootLayout']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()  # 持仓页显示更多
        self.driver.find_element_by_android_uiautomator('text(\"平仓\")').click()  #  平仓
        self.driver.find_element_by_xpath("//*[@resource-id='com.shenzhen.yirabbit:id/tag_group']/android.widget.TextView[2]").click()  # 选择2分之1
        self.driver.find_element_by_id('com.shenzhen.yirabbit:id/sureOpenButton').click()  # 确认平仓
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator('text(\"查看持仓\")').click()  # 查看持仓
        time.sleep(3)

        # 第二次平仓0.05手
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/rootLayout']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()  # 持仓页显示更多
        self.driver.find_element_by_android_uiautomator('text(\"行情\")').click()  # 行情
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*[@resource-id='com.shenzhen.yirabbit:id/ll_profit_loss']").click()  # 行情页展示更多
        self.driver.find_element_by_xpath("//*[@resource-id='com.shenzhen.yirabbit:id/rootLayout']").click()  # 行情页展示订单
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('text(\"平仓\")').click()  # 平仓
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.shenzhen.yirabbit:id/sureOpenButton').click()  # 确认平仓
        self.driver.find_element_by_android_uiautomator('text(\"查看持仓\")').click()  # 查看持仓

    @allure.story('市价卖出 澳元兑日元 平仓')
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    def test_market_sell(self):
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  # 去下单
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()  # 外汇
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()  # 澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"卖出\")').click()  # 卖出澳元兑日元
        self.driver.find_element_by_xpath("//*[@resource-id='com.shenzhen.yirabbit:id/labels']/android.widget.TextView[2]").click()  # 开仓0.2手
        self.driver.find_element_by_android_uiautomator('text(\"确认开仓\")').click()  # 确认开仓
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.shenzhen.yirabbit:id/viewPendingOrder').click()  # 查看持仓
        self.driver.implicitly_wait(10)

        # 第一次平仓0.05手
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/rootLayout']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()  # 持仓页显示更多
        self.driver.find_element_by_android_uiautomator('text(\"平仓\")').click()      #  平仓
        self.driver.find_element_by_xpath("//*[@resource-id='com.shenzhen.yirabbit:id/tag_group']/android.widget.TextView[2]").click()  # 选择2分之1
        self.driver.find_element_by_id('com.shenzhen.yirabbit:id/sureOpenButton').click()   #  确认平仓
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator('text(\"查看持仓\")').click()  # 查看持仓
        time.sleep(3)

        # 第二次平仓0.05手
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/rootLayout']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()  # 持仓页显示更多
        self.driver.find_element_by_android_uiautomator('text(\"行情\")').click()  # 行情
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*[@resource-id='com.shenzhen.yirabbit:id/ll_profit_loss']").click()  # 行情页展示更多
        self.driver.find_element_by_xpath("//*[@resource-id='com.shenzhen.yirabbit:id/rootLayout']").click()  # 行情页展示订单
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('text(\"平仓\")').click()  # 平仓
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.shenzhen.yirabbit:id/sureOpenButton').click()  # 确认平仓
        self.driver.find_element_by_android_uiautomator('text(\"查看持仓\")').click()  # 查看持仓

    @allure.story('限价买入 澳元兑日元 撤单')
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    def test_limit_buy(self):
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  # 去下单
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()  # 外汇
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()  # 澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"买入\")').click()  # 买入澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"挂单\")').click()  # 挂单
        self.driver.find_element_by_android_uiautomator('text(\"限价\")').click()  # 限价
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/xianjiaView']/android.widget.LinearLayout/android.widget.ImageView[1]").click()  # 停损买入设置价格 “-”
        time.sleep(0.2)
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/xianjiaView']/android.widget.LinearLayout/android.widget.ImageView[1]").click()
        self.driver.find_element_by_android_uiautomator('text(\"确认挂单\")').click()  # 确认挂单
        self.driver.find_element_by_android_uiautomator('text(\"查看挂单\")').click()  # 查看挂单
        self.driver.find_element_by_android_uiautomator('text(\"限价挂单\")').click()  # 限价挂单
        self.driver.find_element_by_android_uiautomator('text(\"撤单\")').click()  # 限价撤单
        self.driver.find_element_by_android_uiautomator('text(\"确认\")').click()  # 确认撤单

    @allure.story('限价卖出 澳元兑日元 撤单')
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    def test_limit_sell(self):
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  # 去下单
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()  # 外汇
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()  # 澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"卖出\")').click()  # 卖出澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"挂单\")').click()  # 挂单
        self.driver.find_element_by_android_uiautomator('text(\"限价\")').click()  # 限价
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/xianjiaView']/android.widget.LinearLayout/android.widget.ImageView[2]").click()   # 限价买入设置价格 “+”
        time.sleep(0.2)
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/xianjiaView']/android.widget.LinearLayout/android.widget.ImageView[2]").click()   # 限价买入设置价格 “+”
        self.driver.find_element_by_android_uiautomator('text(\"确认挂单\")').click()  # 确认挂单
        self.driver.find_element_by_android_uiautomator('text(\"查看挂单\")').click()  # 查看挂单
        self.driver.find_element_by_android_uiautomator('text(\"限价挂单\")').click()  # 限价挂单
        self.driver.find_element_by_android_uiautomator('text(\"撤单\")').click()  # 限价撤单
        self.driver.find_element_by_android_uiautomator('text(\"确认\")').click()  # 确认撤单

    @allure.story('停损买入 澳元兑日元 撤单')
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    def test_stop_buy(self):
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  # 去下单
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()  # 外汇
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()  # 澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"买入\")').click()  # 买入澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"挂单\")').click()  # 挂单
        self.driver.find_element_by_android_uiautomator('text(\"停损\")').click()  # 停损
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/xianjiaView']/android.widget.LinearLayout/android.widget.ImageView[2]").click()  # 停损买入设置价格 “+”
        self.driver.find_element_by_android_uiautomator('text(\"确认挂单\")').click()  # 确认挂单
        self.driver.find_element_by_android_uiautomator('text(\"查看挂单\")').click()  # 查看挂单
        self.driver.find_element_by_android_uiautomator('text(\"停损挂单\")').click()  # 限价挂单
        self.driver.find_element_by_android_uiautomator('text(\"撤单\")').click()  # 限价撤单
        self.driver.find_element_by_android_uiautomator('text(\"确认\")').click()  # 确认撤单

    @allure.story('停损卖出 澳元兑日元  撤单')
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    def test_stop_sell(self):
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/closeImage").click()  # 关闭活动弹窗
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/priceRadioButton").click()  # 交易
        self.driver.find_element_by_id("com.shenzhen.yirabbit:id/placeOrderButton").click()  # 去下单
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_android_uiautomator('text(\"外汇\")').click()  # 外汇
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator('text(\"澳元兑日元\")').click()  # 澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"卖出\")').click()  # 卖出澳元兑日元
        self.driver.find_element_by_android_uiautomator('text(\"挂单\")').click()  # 挂单
        self.driver.find_element_by_android_uiautomator('text(\"停损\")').click()  # 停损
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.shenzhen.yirabbit:id/xianjiaView']/android.widget.LinearLayout/android.widget.ImageView[1]").click()  # 停损买入设置价格 “-”
        self.driver.find_element_by_android_uiautomator('text(\"确认挂单\")').click()  # 确认挂单
        self.driver.find_element_by_android_uiautomator('text(\"查看挂单\")').click()  # 查看挂单
        self.driver.find_element_by_android_uiautomator('text(\"停损挂单\")').click()  # 停损挂单
        self.driver.find_element_by_android_uiautomator('text(\"撤单\")').click()  # 限价撤单
        self.driver.find_element_by_android_uiautomator('text(\"确认\")').click()  # 确认撤单

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    #pytest.main(['--alluredir', './app_report'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./app_report -o ./app_report --clean')





