# list
# classname = ['mike','jerry','bob']
# print(classname[0]) # 读取列表中的值，括号中为对应列表中的索引
#
# classname = ['mike','jerry','bob']
# classname[0]= 'hehe'  # 更新列表中的数据，括号中为对应列表中的索引
# print(classname)
#
# classname = ['mike','jerry','bob']
# del classname[0]
# print(classname)   # 删除列表元素,括号中为对应列表中的索引



# 函数1
# def 函数名（参数列表）:
      #函数体
# def print_welcome(name):    # 定义一个Print_welcome的函数，该函数只需要传一个参数“name”
#     print('welcome:',name)   # 等传过来参数之后，我让这个函数干什么事，我让这个函数打印 ‘welecome:’的信息
# print_welcome('jerry')   #  我调用了这个print_welcome的函数，括号里是我给他传的参数，jerry ,最后就打印出了这个结果



# 函数2
# def area(width, height):
#     return width * height
# w = 4
# h = 8
# print('这是我算出来的面积：',area(w , h ))  # area(w, h) 可以看做是一个整体，可以理解为一个变量a，a = area(w, h),
# 最终的结果就是：print(a)，所以可以写成上面的写法 print('这是我算出来的面积：',a)  由于函数体不是直接print 而是用的是return
# return的作用是运行加减乘除的,最后在一起打印出来

# return的用法  return是返回的意思 print 是打印结果的意思
# def plus(a,b):  # 自定义一个 plus的函数，必须要传2个参数 a 和 b
# #     return a+b   # reutrn 返回出 a+b的结果   但是此时是不会打印出来
# # print(plus(2,6))  #  这里才是打印出来


#  求和的
# sum = 0
# for i in [1,2,3,4]:  #首先定义sum=0，是为了第一次i取值时取的是i的最正确的值，也就是i+0=i，后面的结果是这么算的：
#     sum += i           # sum = sum+i = 1
# print(sum)             # sum = 1+2 = 3
#                        # sum = 3+3 = 6
#                        # sum = 6+4 = 10   最后就能得出这个结果等于10


# #  调用函数
# from abstest import my_abs    # 这里我是在调用 abstest （文件名，不含.py的扩展名  导入 my_abs这个函数名来获取的）
# print(my_abs(-888))           # 注意一定要在同一个目录文件下，不在同一个目录文件下是调用不了的


#  位置参数

# def power(x ,n):     #  这里首先记住是必须传了2个参数，循环了2次，第一次是 n =2 循环了一次，s=5  n=1 继续循环了一次第二次
#     s = 1            #   n=1的时候还循环了一次
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5 ,2))


# 可变参数                 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# def calc(*number):       #  这是位置参数的用法，就是我不知道我要传多少个参数，我用一个*号来表示，里面可以是列表或者是元组
#     sum = 0              # 下面的函数就是一个求各个数的平方数之和，我调用参数的时候这里可以传很多个参数
#     for i in number:
#         sum = sum + i * i
#     return sum
# a = calc(1,2,4)
# print(a)


#关键字参数1                       而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# def person(name ,age ,**kw):      #  这个**kw  是关键字参数，可以预先定义一个完整的字典，然后传到**kw里面
#     print("name:",name, "age:",age ,"othoer:",kw)
# a = person("jerry", 27)
# print(a)


# #关键字参数2
# a = {'city':'beijing', 'job':'engineer'}      #  这个是关键字参数的另一种用法，提前定义一个字典，调用函数的时候，直接用**
# def person(name , age , **kw):                #  加你之前定义的那个字典就可以使用了，和上面的使用效果是一样的
#     print('name:',name , 'age:', age , 'other:', kw)
# a = person('jerry', 24 , **a)
# print(a)
# #关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者
# # 愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字
# # 参数来定义这个函数就能满足注册的需求。


# 装饰器

# def logger (func):
#     def wrapper(*args , **kw):
#         print('我准备开始计算：{}函数了:'.format(func.__name__))
#
#         # func(*args , **kw)
#
#         print('计算结束')
#     return wrapper()
#
# @logger
# def add(x ,y):
#     print('{} +{} = {]' .format(x ,y, x+y))
# a = add(200, 500)
# print(a)




