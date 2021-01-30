def test1():
    print('tst1开始了')
    print('tst1结束了')


def test2():
    print('test2开始了')
    test1()
    print('test2结束了')


test2()


# 求n~m之间所有整数之和
def add(n, m):
    x = n
    for i in range(n, m):
        x += i
    return x


result = add(0, 101)
print(result)


# 求n的阶乘

def fac(n):
    x = 1
    for i in range(x, n + 1):
        x *= i
    return x


print(fac(5))


# 计算m阶乘的和m = 6  m = 6 1!+2!+3!+4!+5!+6!
def fac_sum(m):
    x = 0
    for i in range(1, m + 1):
        x += fac(i) #调用上面的函数
    return x
print(fac_sum(5))
