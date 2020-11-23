# map是让函数里面每一个元素都执行函数里面的操作 加减乘除
age = [12, 23, 30, 17, 16, 22, 19]
x = map(lambda ele: ele + 2, age)
adult = list(x)
print(adult)  # [14, 25, 32, 19, 18, 24, 21]