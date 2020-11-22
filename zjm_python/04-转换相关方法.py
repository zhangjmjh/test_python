import json

# 内置函数 eval 可以执行字符串里面的代码
# a ='input("请输入您的用户名")'
# print(a)
# print(eval(a))

# json.dumps()  将字典 元素 列表 集合 元组 转换成json字符串
# person = {'name': 'zhangsan', 'age': 18}  # 字典
# m = json.dumps(person)
# print(m)  # {"name": "zhangsan", "age": 18} 字符串

# json.loads()  将json字符串转换成python里的数据类型
# n = '{"name":"lisi","age":20}'
# s = json.loads(n)
# print(s)  # {'name': 'lisi', 'age': 20}

# 函数
def add(a: int, b: int):
    return a+b
a = add(3, 4)
print(a)
