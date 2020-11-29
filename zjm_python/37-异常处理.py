# 异常捕获  格式如下：

# try:
#     fiel = open('123.txt', 'r')  # 这里因为找不到这个文件夹，所以用异常捕捉能拦截报错，让程序还可以继续运行下去
#
# except IOError:  # 表示如果是 IOError 这种类型的错误就直接pass IOError:文件没找到，属于IO异常，也就是输入输出异常
#     pass  # 捕获异常后 执行的代码

# 举例2个错误
# try:
#     fiel = open('123.txt', 'r')
#     print(num)
# except  (NameError,IOError):  # 因为num没有被定义 不属于 IOError 这种异常 所以异常类型要想被捕获就需要一致
#     print('产生错误了')  # 产生错误了

# 举例捕获所有的异常
# try:
#     fiel = open('123.txt', 'r')
#     print(num)                # result 变量名 也就是报错的结果
# except  Exception as result:  # Exception 表示直接捕获所有的异常
#     print('产生错误了')  # 产生错误了
#     print(result)  # [Errno 2] No such file or directory: '123.txt'

# try 的多层嵌套
import time
try:
    file = open('test_file.txt','r')
    try:
        while True:
            content = file.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:  # 用这个写法的代码表示程序是否报错都会执行
        file.close()
        print('文件关闭')
except Exception as result:
    print('发生异常')