#  列表
list=['luoahong','chenqun','wenhai','daiqiao','xiedi','guiwei']

# 1、取值
# a = list[0]
# print(a)     #  结果：luoahong

# 2、切片
# a = list[1:3]
# print(a)    #  结果：['chenqun', 'wenhai']

# 3、增加元素
# list.append("haha")
# print(list)   #  结果：['luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei', 'haha']

# 4、指定位置插入元素
# list.insert(0, "xxx")
# print(list)    #  结果：['xxx', 'luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 5、修改
# list[0] = "zjm"
# print(list)    #  结果：['zjm', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 6、 删除
# list.remove('guiwei')
# print(list)   #  结果：['luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi']

# list.pop(0)
# print(list)   # 结果：['chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 7、排序
# list.sort();
# print(list)  # 结果： ['chenqun', 'daiqiao', 'guiwei', 'luoahong', 'wenhai', 'xiedi']

# list.sort(reverse=True)  #   降序
# print(list)   #  结果： ['xiedi', 'wenhai', 'luoahong', 'guiwei', 'daiqiao', 'chenqun']

# 8、获取下标
# a = list.index('luoahong')
# print(a)   # 结果：  0

# 9、列表去重
# list1 = ['1','1','2','2','3','3','3']
# list1 = list(set(list1))
# print(list1)   # 结果：['3', '2', '1']


# 元组
tup = (1, 2, ['a', 'b', 'c'], 'd', 'e', ('gu', 'tang'), 1)

# 1、查询
# print(tup[0])    # 结果：1

# 2、列表转换成元组
# list = ["python book","Mac","bile","kindle"]
# tup = tuple(list)
# print(tup)   # 结果：('python book', 'Mac', 'bile', 'kindle')

# 3、计算元组中元素的长度
# print(len(tup))  # 结果： 6

# 4、统计元素个数
# print(tup.count(1))    # 结果：  2

# 字典
dict = {"color":"green","points":5}

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

# 4、


# 5、pop 删除指定的键
# dict.pop("color")
# print(dict)  # 结果：{'points': 5}

# 6、输出 key 和 value
# dict = {"color":"green","points":5}
# for i in dict.keys():
#     print(i)  # 结果： color points
# for i in dict.values():
#     print(i)  # 结果：green  5
