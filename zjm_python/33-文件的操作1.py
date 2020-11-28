# open 参数介绍
# file 用来指定打开的文件
# mode 打开文件时的模式 
# encoding 打开文件时的编码方式
# 绝对路径: 从电脑硬盘读取的路径
# 相对路径: 当前文件所在的文件夹开始的路径
# ../ 表示返回到上一级文件夹

# 相对路径写法
# file = open('test_file.txt', encoding='utf-8')
# print(file.read())
# file.close()

# 绝对路径写法  前面加r是避免\转义
file= open(r'E:\zhangjm_python\zjm_python\test_file.txt', encoding='utf-8')
print(file.read())
# file.close()