

from test_po.page.BasePage import BasePage
from test_po.page.SearchPage import SearchPage

class MainPage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_name("q").send_keys(keyword)
        self.driver.find_element_by_css_selector(".nav__search button").click
        return SearchPage(self.driver)
