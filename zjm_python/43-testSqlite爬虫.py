import sqlite3
# python3里面自带的一个轻型的数据可库

conn = sqlite3.connect('test.db')  #  打开或创建数据库文件
print('创建成功')