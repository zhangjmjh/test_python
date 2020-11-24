# 导入了demo模块的函数 注意使用的过程中要加函数名才可以使用
import demo

print(demo.a)  # hello
print(demo.ret())  # my_module的test方法
print(demo.foo())  # my_module的foo方法

#  以下内容是demo.py的内容
a = 'hello'

def ret():
    print("my_module的test方法")



def foo():
    print('my_module的foo方法')


# __name__ 当直接运行这个py文件的时候，值是__main__  这端代码是直接运行才能执行的
# 如果这个py文件作为一个模块导入的时候，值是文件名
if __name__ == '__main__':
    print('my_module函数的结果')