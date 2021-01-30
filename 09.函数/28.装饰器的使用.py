# 开放封闭原则，
# 已经写好的代码，能不要改，就不要改

def can_play(fn):
    def inner(x, y, *args, **kwargs):
        print(args)
        # if args[0] <= 22:
        clock = kwargs.get('clock',23) #不告诉时间，默认就不让玩游戏
        if clock <= 22:
            fn(x, y)
        else:
            print('太晚了，赶紧睡觉')

    return inner


@can_play
def play_game(name, game):
    print('{}正在玩{}'.format(name, game))

# play_game('张三', '王者荣耀')
# play_game('张三', '绝地求生')

play_game('张三', '王者荣耀')
play_game('张三', '绝地求生', clock=18 )
