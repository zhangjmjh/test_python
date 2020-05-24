from zjm_page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    def follow(self, keyword):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div[1]/table/tr[3]/td[6]/a/i').click
        return self