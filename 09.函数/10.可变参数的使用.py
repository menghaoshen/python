def add(a, b):
    return a + b


def add_many(m):
    x = 0
    for i in m:
        x += i
    return x


nums = [1, 2, 3, 4, 5, 6, ]
print(add_many(nums))
print(add_many((1, 2, 3, 4, 5, 6, 7, 8)))
print(add_many({5, 6, 7, 8, 1, 3}))

#一次input只能接收一次用户的输入
x = input('请输入多个数字，中间使用逗号分开')
print(x)
nums = x.split(',')
print(nums)
