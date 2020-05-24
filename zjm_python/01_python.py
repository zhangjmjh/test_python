

import requests
import json

class RunMain:
    """
    封装请求方法的类
    """

    def send_get(self, url ,data):
        r = requests.get(url = url ,params = data).json()
        return r

    def send_post(self, url ,data):
        r = requests.post(url = url ,data = data).json()
        return r

    def run_main(self, url ,methon ,data= None):
        r = None
        if methon == 'GET':
            r = self.send_get(url, data)
        else:
            r = self.send_post(url, data)
        return r

if __name__ == '__main__':
    url = 'http://web.juhe.cn:8080/finance/stock/hs'
    data = {'key':'1c705503c9bc44c87227fdfb854557c6', 'gid': 'sh601009'}
    run = RunMain()
    print(run.run_main(url ,'GET' , data))


def person(name, age, **kw):
    print('name:', name , 'age:',age , 'other:', kw)
person('jack', 18)

class Student(object):
    def __init__(self , name , score):
        self.name = name
        self.score = score
bart = Student('jack' , 99)
print(bart.name)

class Student1(object):
    def __init__(self , name , score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%d'%(self.name , self.score))
bart = Student('jack' , 99)
print(bart.score)

