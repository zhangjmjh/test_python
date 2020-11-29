import urllib.request
import urllib.parse

# get请求
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8')) #  把网页源码进行utf-8解码

# post请求  bytes 表示用字节的方式
# data = bytes(urllib.parse.urlencode({'hello':"world"}),encoding="utf-8")
# response = urllib.request.urlopen('http://httpbin.org/post',data = data)
# print(response.read().decode('utf-8'))

# 超时怎么办
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=10)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print('time out!')

# 获取头部
# response = urllib.request.urlopen('http://www.baidu.com')
# # print(response.getheaders())
# print(response.getheader('server'))  # BWS/1.1 表示获取单个参数

# 尝试模拟浏览器访问
# url = 'http://httpbin.org/post'
# headers={
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name':"eric"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# 访问豆瓣
url = 'https://www.douban.com/'
headers={  # 这里加上浏览器的User-Agent信息就可以躲过豆瓣的提示了
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))