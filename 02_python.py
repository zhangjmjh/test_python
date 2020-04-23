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
