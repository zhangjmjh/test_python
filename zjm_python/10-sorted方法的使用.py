# sorted 可以对列表和元组进行排序

# ints = (5, 7, 3, 2, 9, 4)
# x = sorted(ints)
# print(x)

# sort 高级用法 给列表里面的字典来排序
student =[{'name':'jerry','age':80},{'name':'herry','age':10}]
student.sort(key=lambda ele:ele['name'])
print(student)