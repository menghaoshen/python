def test(a, b):
    x = a + b
    return x  # 表示函数结束
    return 'hello'  # 这段代码不会被执行，一般情况下，一个函数只能执行一个return


def demo(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        print('除数不能为0')
    else:
        return x
    finally:
        return 'good' #如果函数里面有finall，finall 会覆盖前面的返回值


print(demo(1, 0))
