from bs4 import BeautifulSoup

file = open('./baidu.html',encoding='UTF-8')  # 打开
html = file.read()  # 读取
bs = BeautifulSoup(html,'html.parser')  # 解析

# print(bs.title)  # <title>百度一下，你就知道 </title>

# print(bs.title.string)  # 百度一下，你就知道

# print(bs.a)  # <a class="mnav" href="http://news.baidu.com" name="tj_trnews"><!--新闻--></a>

# print(type(bs))  # <class 'bs4.BeautifulSoup'>

# print(bs)  #  整个文档

# print(bs.a.string)  # 新闻

# 文档的遍历
# print(bs.head.contents)  # 获取Tag的所有子节点 返回一个list
# print(bs.head.contents[1])


# 文档的搜索

# 搜索的方法：查找所有的a标签 字符串过滤:会查找与字符串完全匹配的内容
# t_list = bs.find_all('a')
# print(t_list[1])  # <a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>

# 搜索的方法 kwargs  参数
# t_list = bs.find_all(id='head')
# t_list = bs.find_all(href="//www.baidu.com/more/")

# for i in t_list:
#     print(t_list)  #  打印所有id=head标签的内容

import re
# 搜索的方法 text 参数
t_list = bs.find_all(text='hao123')
t_list = bs.find_all(text=re.compile('\d'))  # 应用正则表达式来查找包含特定文本的内容(标签里的字符串)

# for i in t_list:
#     print(i)  # hao123
#     print(i)  # hao123  爬虫功能

# limit 参数
# t_list = bs.find_all('a',limit=3)
# for i in t_list:
#     print(i)
# <a class="mnav" href="http://news.baidu.com" name="tj_trnews"><!--新闻--></a>
# <a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
# <a class="mnav" href="https://www.hao123.com" name="tj_trhao123">hao123</a>

# css选择器
t_list = bs.select('title')  # 通过标签来查找
print(t_list)  # [<title>百度一下，你就知道 </title>]