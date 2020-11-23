import time

def cal_time(fn):
    def inner(x, *args, **kwargs):  # x = 10000
        start = time.time()
        s = fn(x)  #  等于demo 函数  x=10000 传递给  n
        end = time.time()
        print('总共需要的时间{}'.format(end - start))
        return s
    return inner

@cal_time
def demo(n):  #  n=10000
    x = 0
    for i in range(1, n):
        x += i
    return x
m = demo(10000, 'good', y='hello')
print('m的值是', m)
