# 最少两个参数
def add(a, b, *args, nul=1, **kwargs):  # *args 表示可变的位置参数 ,**kwarge 表示可变的关键字参数
    print('a = {},b = {}'.format(a, b))
    print('args = {}'.format(args))  # 多出来的位置参数，会以元组的形式保持到args里面
    print('kwargs={}'.format(kwargs))  # 多出来的关键字参数会以字典的形式保存
    c = a + b
    for arg in args:
        c += arg
    return c * nul


print(add(1, 3, nul=2, x=3, y=4))
print(add(1, 3, 4, 5, 6))
print(add(1, 3, 4, 5, 6, 7, 8, 8, 9, 10))


# 一个没有也可以
def add(*agrs):
    pass
