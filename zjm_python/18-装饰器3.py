# 装饰器固定结构  固定写法  需求：如果超过22点不让玩游戏  如果没传参数就默认是xxx点
def can_play(fn):
    def inner():
        pass

    return inner


# 装饰器举例
def can_play(fn):
    def inner(x, y, *args, **kwargs):  # x=张三  y=王者荣耀
        if args[0] <= 22:
            fn(x, y)  # 回调play_game 把x=张三  y=王者荣耀  传给  name  game
        else:
            print('太晚了，不能玩游戏了')

    return inner


@can_play
def play_game(name, game):  # 把x=张三  y=王者荣耀  传给  name  game
    print('{}正在玩{}'.format(name, game))


play_game('张三', '王者荣耀', 18)  # 张三正在玩王者荣耀
play_game('张三', '王者荣耀', 23)  # 太晚了，不能玩游戏了


# # 装饰器举例      用上 **kwargs 的写法
def can_play(fn):
    def inner(x, y, *args, **kwargs):  # x=张三  y=王者荣耀
        clock = kwargs.get(clock, 23)  # 拿到 clock的值 如果用户没传 默认23
        if clock <= 22:
            fn(x, y)  # 回调play_game 把x=张三  y=王者荣耀  传给  name  game
        else:
            print('太晚了，不能玩游戏了')

    return inner


@can_play
def play_game(name, game):  # 把x=张三  y=王者荣耀  传给  name  game
    print('{}正在玩{}'.format(name, game))


play_game('张三', '王者荣耀', clock=23)  # 太晚了，不能玩游戏了
play_game('张三', '王者荣耀', clock=23)  # 太晚了，不能玩游戏了
