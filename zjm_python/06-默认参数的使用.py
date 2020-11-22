# end=""  就是一个缺省参数  默认就是换行

print('hello world', end="")
print('hello world')


def say_hello(name, age, city="湖南"):
    print('我叫{},今年{},我来自{}'.format(name, age, city))

say_hello('jerry',21)
