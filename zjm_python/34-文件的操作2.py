# mode 打开文件时的模式

# r 只读模式 默认
# file = open('test_file.txt','r',encoding='utf8')
# print(file.read())  # 测试
# file.close()

# w 写入模式 如果文件存在，会覆盖文件，如果不存在，会创建
# file = open('test_file.txt','w')
# file.write('呵呵')

# b 以二进制读取
# rb 以二进制读取   wb 以二进制写入
# file = open('test_file.txt','rb')
# print(file.read())  # b'\xba\xc7\xba\xc7' 结果是二进制

file = open('test_file.txt','wb')
file.write('大家好'.encode('utf8'))

