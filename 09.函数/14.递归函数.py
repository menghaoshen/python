# 递归简单来说，就是函数内部自己调用自己的
# 递归最重要的是找到出口(停止的条件)
# def test():
#     print('test')
#     test()


count = 1


def tell_story():
    global count  # 局部的变量要用外部的变量，要用global
    count += 1
    print('------------------', count)
    print('从前有个山')
    print('山上有个庙')
    print('庙里有个老和尚')
    print('还有一个小和尚')
    print('老和尚在给小和尚讲故事')
    print('故事的内容是')
    if count < 5:
        tell_story()


tell_story()


# 求1到n的和
def get_sum(n):
    if n == 0: #到0就停止
        return 0 #出口
    return get_sum(n - 1) + n

print(get_sum(2))
