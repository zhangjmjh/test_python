from bs4 import BeautifulSoup  # 网页解析，获取数据
import re   # 正则表达式，进行文字匹配
import urllib.request,urllib.error  # 制定url,获取网页数据
import xlwt  # 进行excel 操作
import _sqlite3 # 进行SQlite 数据库操作



def main():
    baseurl = 'https://movie.douban.com/top250?start='
    # 1 爬取网页
    datalist = getDate(baseurl)
    savepath = r'./豆瓣电影Top250.xls'
    # 3 保存数据
    # saveData(savepath)
    askURL('https://movie.douban.com/top250?start=')



# 得到指定一个URL的网页内容
# head 表示告诉豆瓣 我们是什么类型的服务器
def askURL(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,reason):
            print(e.reason)

    return html  # 这里一定要返回给这个网页 给这个传递的网页

# 爬取网页
def getDate(baseurl):
    datalist = []
    for i in range(0,10): # 调用获取页面信息的函数 10次 一页25条
        url = baseurl + str(i*25)
        html = askURL(url)  # 保存获取到的网页源码
        # 逐一解析数据


    return datalist

# 保存数据
def saveData(savepath):
    pass



if __name__ == '__main__':  # 当程序执行时
    main()