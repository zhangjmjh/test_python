# 递归 其实就是自己调用自己 但是要有一个限制条件
# count = 0
#
#
# def tell_story():
#     global count
#     count += 1
#     print('从前有座山')
#     if count < 5:
#         tell_story()
#
#
# tell_story()


# 用递归求 1-n的和  只要想好出去的路就好了 get_sum分别去取 5  4  3  2  1 最后到0结束条件
# def get_sum(n):
#     if n == 0:
#         return 0
#     return n + get_sum(n - 1)
#
#
# print((get_sum(5)))

# 使用递归求n ! n! =n*(n-1)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(3))  # 3*2*1*1
