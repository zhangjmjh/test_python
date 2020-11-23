import time

def cal_time(fn):  # fn = demo
    start = time.time()
    fn()  # demo() 这里就是要执行的函数，fn()  就是直接调用了这个函数 同时 cal_time必须传一个参数过去
    end = time.time()
    print('代码运行的时间{}秒'.format(end - start))

def demo():
    x = 0
    for i in  range(1,1000000):
        x += i
    print(x)

def foo():
    print('hello')
    time.sleep(3)
    print('world')

cal_time(demo)
cal_time(foo)

# 499999500000
# 代码运行的时间0.11095046997070312秒
# hello
# world
# 代码运行的时间3.0000693798065186秒