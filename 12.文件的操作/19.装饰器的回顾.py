def can_play(fn):
    print('外部函数被调用了')
    def inner(name,game,**kwargs):
        clock = kwargs.get('clock',21)
        if clock >= 21:
            print('太晚了不能玩游戏了')
        else:
            fn(name,game)
    return inner

@can_play
def paly_game(name,game):
    print(name + '正在玩' + game)


paly_game('张三','王者荣耀',clock=22)