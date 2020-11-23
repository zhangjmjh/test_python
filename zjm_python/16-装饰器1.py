import time


def cal_time(fn):
    def inner():
        start = time.time()
        fn()  # 这里实际上就去调了demo()  函数
        end = time.time()
        print('代码耗时{}'.format(end - start))
    return inner

@cal_time
# 这里所做的事
# 1、调用cal_time函数
# 2、会把  demo 传递给  fn  同时会把  fn 又传递给了 demo() 函数  等于事2个函数互换
def demo():
    x = 0
    for i in range(1,100):
        x += i
    print(x)
demo()