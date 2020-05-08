# 装饰器

def logger (func):
    def wrapper(*args , **kw):
        print('我准备开始计算：{}函数了:'.format(func.__name__))

        # func(*args , **kw)

        print('计算结束')
    return wrapper()

@logger
def add(x ,y):
    print('{} +{} = {]' .format(x ,y, x+y))
a = add(200, 500)
print(a)