# 字符串
a = 'afasdfasdf'

# 1、访问字符串中的值
var1 = 'Hello World!'
# print(var1[0]) # 结果：H

# 2、字符串连接
var1 = 'Hello World!'
# print(var1+'haha') # 结果：Hello World!haha

# 3、格式化字符串  %s 格式化字符串  %d 格式化整数
# print("My name is %s and weight is %d kg!" % ('Zara', 21))
# 结果：My name is Zara and weight is 21 kg!

# 4、字符串切片
txt = "Google#Runoob#Taobao#Facebook"
x = txt.split("#", 1)  # 以#号作为分割 第二个参数为 1，返回两个参数列表
# print(x)  # ['Google', 'Runoob#Taobao#Facebook']

# 5、将数字转换成字符串
tt = 322
tem = '%d' % tt
# print(tem)  # 322
# print(type(tem))  # <class 'str'>

#  列表
list = ['luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 1、取值
a = list[0]
# print(a)     #  结果：luoahong

# 2、切片
a = list[1:3]
# print(a)    #  结果：['chenqun', 'wenhai']

# 3、增加元素
list.append("haha")
# print(list)   #  结果：['luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei', 'haha']

# 4、指定位置插入元素
list.insert(0, "xxx")
# print(list)    #  结果：['xxx', 'luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 5、修改
list[0] = "zjm"
# print(list)    #  ['zjm', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 6、 删除
list.remove('guiwei')
# print(list)   # ['luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi']

list.pop(0)  # 删除指定位置的元素
# print(list)   # ['chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 7、排序
list.sort();
# print(list)  #  ['chenqun', 'daiqiao', 'guiwei', 'luoahong', 'wenhai', 'xiedi']

list.sort(reverse=True)  # 降序
# print(list)   #  ['xiedi', 'wenhai', 'luoahong', 'guiwei', 'daiqiao', 'chenqun']

# 8、获取下标
# a = list.index('luoahong')
# print(a)   # 0

# 9、列表去重
list1 = ['1', '1', '2', '2', '3', '3', '3']
# list1 = list(set(list1))
# print(list1)   # ['3', '2', '1']

# 10、sort 高级用法 给列表里面的字典来排序
student = [{'name': 'jerry', 'age': 80}, {'name': 'herry', 'age': 10}]
# student.sort(key=lambda ele: ele['name'])  # ele 可以随意定义
# print(student)
# 结果：[{'name': 'jerry', 'age': 80}, {'name': 'herry', 'age': 10}]

# 元组
tup = (1, 2, ['a', 'b', 'c'], 'd', 'e', ('gu', 'tang'), 1)

# 1、查询
# print(tup[0])    # 结果：1

# 2、列表转换成元组
list = ["python book", "Mac", "bile", "kindle"]
# tup = tuple(list)
# print(tup)   # 结果：('python book', 'Mac', 'bile', 'kindle')

# 3、计算元组中元素的长度
# print(len(tup))  # 结果： 6

# 4、统计元素出现的个数
# print(tup.count(1))    # 结果：  2

# 字典
dict = {"color": "green", "points": 5}


# 1、查
# print(dict["color"])   # 结果：green

# a = dict.get("color")  查 get()
# print(a)  # 结果： green

# 2、增加
# dict["token"] = "123"
# print(dict)   # 结果： {'color': 'green', 'points': 5, 'token': '123'}

# 3、改
# dict["token"] = "456"
# print(dict)   # 结果： {'color': 'green', 'points': 5, 'token': '456'}

# 4、pop 删除指定的键
# dict.pop("color")


# print(dict)  # 结果：{'points': 5}

# 5、输出 key 和 value
# dict = {"color":"green","points":5}
# for i in dict.keys():
#     print(i)  # 结果： color points
# for i in dict.values():
#     print(i)  # 结果：green  5


# 冒泡小程序
# list = [5, 23, 3, 2, 54, 4, 6, 8, 856]
# list_len = len(list)
#
# for i in range(list_len - 1):
#     for j in range(i, list_len):
#         if list[i] > list[j]:
#             list[i], list[j] = list[j], list[i]
# print(list)  # 结果：[2, 3, 4, 5, 6, 8, 23, 54, 856]


# 1-100之间的偶数
# sum1 = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sum1 = sum1 +i
# print('1-100之间偶数的和是:''%d'%(sum1))


# 左下三角格式输出九九乘法表
# for i in range(1,10):
#     for j in range(1,1+i):
#        print("%d*%d=%d" % (i,j,i*j),end=" ")
#     print (" ")


# 获取某个字符串出现位置和次数
# def getStrInfo(str, target):
#     count = 0
#     for index, i in enumerate(str):
#         if target == i:
#             count += 1
#             print(target, '出现的位置:', index)  # 出现的位置
#     print(target, '出现的次数:', count)  # 出现的次数
# getStrInfo("asfafaadfa", "a")


# enumerate 在字典上是枚举、列举的意思 参数为可遍历/可迭代的对象(如列表、字符串)
# enumerate 多用于在for循环中得到计数，利用它可以同时获得索引和值，即需要index和value值的时候可以使用
# def get_number(ret, clc):
#     count = 0
#     for i, value in enumerate(ret):
#         if value == clc:
#             count += 1
#             print(clc, "出现的位置", i)
#     print(clc, "出现的次数", count)
# get_number("afasfasdf", "a")

# enumerate 方法举例
# a = "afasfasdf"
# for i in enumerate(a):
#     print(i)
# 结果
# (0, 'a')
# (1, 'f')
# (2, 'a')
# (3, 's')
# (4, 'f')
# (5, 'a')
# (6, 's')
# (7, 'd')
# (8, 'f')

# 编写一个函数，求多个数中的最大值
# def get_max(*args):
#     x = args[0]
#     for i in args:
#         if i > x:
#             x = i
#     return x
# print(get_max(3, 8, 9, 3, 6, 3)) # 9

# 编写一个函数，提取指定字符串中所有的字母，然后拼接在一起组成一个新的字符串
# def new_alphas(word):
#     new_str = ''
#     for i in word:
#         if i.isalpha():
#             new_str += i
#     return new_str
#
#
# print(new_alphas('rwer23232erw'))  # rwererw


# 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘
# def get_factorial(n=10):
#     x = 1
#     for i in range(1, n + 1):
#         x *= i
#     return x
#
#
# print(get_factorial(5))  # 120


# 写一个函数 求多个数的平均值
# def num(*args):
#     x = 0
#     for i in args:
#         x += i
#     return x / len(args)
#
#
# print(num(1, 2, 3))  # 2.0


# 写一个capitalize函数 能够将指定字符串的首字母变成大写字母
def capitalize(str):
    c = str[0]
    if 'z' >= c >= 'a':
        new_str = str[1:]
        return c.upper() + new_str
    return str


print(capitalize('rwerwrw'))  # Rwerwrw


# 写一个endwith函数 判断一个字符串是否以指定的字符串结束
# def endwith(ols_str,str1):
#     if ols_str[-len(str1):] == str1:
#     #     print('是')
#     # else:
#     #     print('否')
#
# endwith('hello','llo')  # 是

# 写一个isdigit函数 判断一个字符串是否是纯数字字符串
def isdigit(str):
    for i in str:
        if not '0' <= i <= '9':
            return False
    return True


print(isdigit('hee99'))  # False


# 写一个自己的max函数 获取序列中元素的最大值 如果序列是字典 获取字典的最大值
def get_max(ret):
    if type(ret) == dict:
        ret = list(ret.values())
    a = ret[0]
    for i in ret:
        if i > a:
            a = i
    return a


print(get_max([2, 5, 8, 6, 3, 1]))  # 8
