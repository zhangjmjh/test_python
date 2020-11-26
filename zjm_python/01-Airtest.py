# 启动APPstart_app
# 停止APP  stop_app()
# 回到桌面   home()
# 查看所有APP安装的第三方APP包名 adb shell am monitor

# all_dev = d.list_app()  # 获取手机上安装的所有APP  列表
# print(all_dev)

# 判断手机是否装了APP
# d = device()
# if i in all_dev:
#     print("已安装")
#     start_app()
# else:
#     adb install

# 无限循环刷视频
while 2:
    swipe()  #  滑动

# poco模式
# screen = poco.get_screen_size()  # 获取当前手机的分辨率
x = screen[0]
y = screen[1]
# swipe((0.8x,0.5y),(0.2x,0.5y))  # 滑动操作

# keyevent("BACK")
# for i in range(100)
# home()
# def student():
# home
# start_app("com.")
