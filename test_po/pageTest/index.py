
from pageTest.base_page import BasePage

class Index(BasePage):

    def __init__(self, driver):
        self.driver = driver


    def goto_register(self):
        #点击立即注册
        self.driver.find_element_by_class_name("index_head_info_pCDownloadBtn").click
        return Register()



    def goto_login(self):
        # 点击企业登录
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click
        return Login()
