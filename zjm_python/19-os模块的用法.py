import os # 调用操作系统里面的方法

# 获取操作系统的名字
print(os.name)  # nt-windows

# abspath 获取文件的绝对路径
print(os.path.abspath('01_python基础.py'))  #E:\zhangjm_python\zjm_python\01_python基础.py

# isdir判断是否是文件夹
print(os.path.isdir('01_python基础.py'))  # False

# isfile 判断是否是文件
print(os.path.isfile('01_python基础.py')) # True

# exists 判断文件是否存在
print(os.path.exists('01_python基础.py')) # True

# os其他方
os.getcwd()  # 查看当前文件路径