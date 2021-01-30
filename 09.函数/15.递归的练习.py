# 使用递归求n！ n!=*(n -1)!
def fact(n):
    if n == 0:
        return 1  # 0的阶层是1 到0就出去
    return n * fact(n - 1)


print(fact(6))


# 使用递归求斐波那契数列第n个数字
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n - 2) + f(n - 1)


print(f(8))
