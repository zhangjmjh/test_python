import requests
import pytest
class Test_api():
    url = 'http://httpbin.org'
    def test_01(self):
        url = self.url + '/get'
        requests.get(url)
        rel = requests.get(url)
        print(rel.status_code)
        print(rel.text)

    def test_02(self):
        url = self.url + '/get'
        params = {'name':'zhangsan','age':18}
        requests.get(url)
        rel = requests.get(url,params=params)
        print(rel.status_code)
        print(rel.text)

    def test_03(self):
        url = self.url + '/get'+'?name=zhangsan&age=18'
        requests.get(url)
        rel = requests.get(url)
        print(rel.status_code)
        print(rel.text)

    def test_04(self):
        url = self.url + '/get'+'?name=zhangsan&age=18'
        requests.get(url)
        rel = requests.get(url)
        print(rel.headers)
        print(rel.cookies)
        print(rel.status_code)
        print(rel.text)